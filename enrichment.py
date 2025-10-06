from typing import Literal

PROMPTS = {
  'nq': {
    'purpose': "Given the following text, describe the purpose of this text in layman's terms in one paragraph.",
    'summary': "Given the following text, summarize this text in layman's terms in one paragraph.",
    'qa': "Given the following text, generate at most 20 distinct question-answer pairs on this text. The questions should be general, and phrased in layman's terms, using vocabulary that can be distinct from the text, but still requires explicit or implicit knowledge from the text. Each question-answer pair should be formatted as a list where the first element is the question and the second element is the answer. The output should be a list of lists in JSON format."
  },
  'bright': {
    'purpose': "Given the following technical text, describe the purpose of this text in layman's terms in one paragraph.",
    'summary': "Given the following technical text, summarize this text in layman's terms in one paragraph.",
    'qa': "Given the following technical text, generate at most 20 distinct question-answer pairs on this text. The questions should be general, and phrased in layman's terms, using vocabulary that can be distinct from the text, but still requires explicit or implicit knowledge from the text. Each question-answer pair should be formatted as a list where the first element is the question and the second element is the answer. The output should be a list of lists in JSON format."
  },
  'table': {
    'purpose': "Given the following table, describe the purpose of this table in layman's terms in one paragraph.",
    'summary': "Given the following table, summarize this table in layman's terms in one paragraph.",
    'qa': "Given the following table, generate at most 20 distinct question-answer pairs on this table that includes both simple questions and those requiring summarization or aggregation. The questions should be phrased in layman's terms, using explicit or implicit knowledge from the table. The question and answer should avoid using exact terms, such as shortened forms, from the table but can instead use naturally phrased language. Each question-answer pair should be formatted as a list where the first element is the question and the second element is the answer. The output should be a list of lists in JSON format."
  }
}

def get_enrichment_prompt(
  dataset: Literal['nq', 'bright', 'table'],
  enrichment_type: Literal['purpose', 'summary', 'qa'],
  object_content: str
):
  prompt = PROMPTS[dataset][enrichment_type]

  if dataset in ['nq', 'bright']:
    none_prompt = 'If you do not think the text is semantically meaningful, output None.'
  else:
    none_prompt = 'If you do not think the table is semantically meaningful, output None.'
  
  return f'{prompt} {none_prompt}\n\n{object_content}'