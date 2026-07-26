---
name: large-language-models
id: 20260726T111531Z
tier: library-topic
domain: technology
author: Researcher-1
tags: [large-language-models, transformers, attention-mechanism, scaling-laws, emergent-abilities, gpt, artificial-intelligence]
links: [library/coding-agentic-ai/agent-skill-systems.md, library/coding-agentic-ai/context-window-management.md]
---

# Large Language Models -- How Next-Token Prediction Trained at Unprecedented Scale Produces General-Purpose Reasoning

Large language models (LLMs) are neural networks built on the
transformer architecture that are trained on vast corpora of text to
predict the next token in a sequence. When scaled to hundreds of
billions of parameters and trained on trillions of tokens, this
apparently simple objective produces models capable of translation,
summarization, code generation, mathematical reasoning, and creative
writing -- abilities that were not explicitly programmed but emerged
from the interaction of scale, data, and architecture. LLMs represent
the most significant advance in artificial intelligence since the
deep learning revolution, and their trajectory -- toward multimodal,
agentic, and increasingly autonomous systems -- is reshaping the
technological and economic landscape.

## Background

The intellectual lineage of LLMs traces back to two converging lines of
research: statistical language modeling and neural network architecture.
Statistical language models, dating to Claude Shannon's work on
information theory in the 1940s, treated language as a probability
distribution over sequences of words. The fundamental task was always
next-word prediction: given a sequence of preceding words, estimate the
probability distribution over possible next words. Early n-gram models
counted co-occurrences but could not generalize beyond patterns they had
explicitly seen.

The deep learning revolution of the 2010s brought neural networks to
language. Recurrent neural networks (RNNs), and later Long Short-Term
Memory networks (LSTMs), could process variable-length sequences and
capture longer-range dependencies than n-gram models. But RNNs processed
tokens sequentially -- each step depended on the previous one -- making
training slow and limiting the context they could practically retain.
Gated architectures helped but did not solve the fundamental problem: the
farther apart two words were in a sequence, the harder it was for the
model to learn their relationship.

The breakthrough came in 2017 when Vaswani et al. published "Attention Is
All You Need," introducing the Transformer architecture. Instead of
processing tokens one by one, the Transformer used a mechanism called
self-attention that allowed every token in a sequence to directly attend
to every other token, in parallel. This eliminated the sequential
bottleneck of RNNs, made training dramatically more parallelizable, and
enabled models to capture dependencies across arbitrarily long distances.
The Transformer was originally designed for machine translation, but its
architecture proved so general and scalable that it became the foundation
for an entire generation of language models.

The second critical insight came from scaling. In 2018, OpenAI's GPT
(Generative Pre-trained Transformer) demonstrated that a Transformer
trained on a large, diverse corpus of internet text could be fine-tuned
for specific tasks with strong results. But the real shock came with
GPT-2 (2019) and especially GPT-3 (2020), which showed that as models
scaled up -- GPT-3 had 175 billion parameters -- they developed the
ability to perform entirely new tasks from just a few examples or even
simple instructions, without any task-specific training. This property,
called in-context learning or few-shot learning, was not designed into
the architecture. It emerged.

Kaplan et al. (2020) formalized the relationship between scale and
performance in their foundational scaling laws paper. They found that
language model loss follows a power law with respect to model size,
dataset size, and compute, across many orders of magnitude. The
implication was profound: if you want a better model, you do not
necessarily need a better architecture or algorithm -- you can simply
scale up the one you have, provided you also scale the data and compute
proportionally.

Hoffmann et al. (2022) refined this picture with the Chinchilla scaling
laws, showing that most large models at the time were significantly
undertrained relative to the optimal ratio. Their compute-optimal model,
Chinchilla (70B parameters), matched or outperformed much larger models
like Gopher (280B) and GPT-3 (175B) by being trained on more data --
roughly 20 tokens per parameter rather than the typical 1-2 tokens per
parameter. This shifted the focus of the field from "make it bigger" to
"train it longer on more data," and influenced the design of subsequent
models including Llama, Mistral, and Claude.

## Core Concepts

### The Transformer Architecture

At the heart of every LLM is the Transformer architecture. A Transformer
processes a sequence of tokens -- words or subword units -- through a
stack of identical layers, each containing two main subcomponents:
multi-head self-attention and a feed-forward network.

Self-attention is the key innovation. Each token is projected into three
vectors: a query (Q), a key (K), and a value (V). For every pair of
tokens, the model computes an attention score by taking the dot product
of the query of one token with the key of another. These scores are
normalized with softmax to produce a probability distribution: how much
should token A "pay attention" to token B? The output for each token is
a weighted sum of all other tokens' value vectors, weighted by the
attention scores. In a single operation, every token can incorporate
information from every other token in the sequence, regardless of
distance.

Multi-head attention runs multiple self-attention operations in parallel,
each with its own learned projection matrices. Different heads learn to
attend to different linguistic relationships: one head might track
subject-verb agreement, another might resolve pronoun references, a
third might capture semantic similarity. The outputs of all heads are
concatenated and projected back to the model's hidden dimension.

Because self-attention is a set operation -- it does not inherently
encode the order of tokens -- Transformers add positional encodings to
the input embeddings. The original paper used sinusoidal functions of
position, but modern LLMs more commonly use learned positional embeddings
or Rotary Position Embeddings (RoPE), which encode relative position
through rotation matrices and generalize better to longer sequences than
seen during training.

The feed-forward network in each layer is typically a two-layer
fully-connected network with a non-linear activation (commonly GELU or
SwiGLU in modern models). While attention handles communication between
tokens, the feed-forward network does the heavy lifting of computation
and knowledge storage. Research has shown that feed-forward layers in
LLMs act as key-value memories, storing factual knowledge learned during
training.

### Decoder-Only Architectures

While the original Transformer had both an encoder (which processes the
input) and a decoder (which generates output), most modern LLMs use a
decoder-only architecture. The GPT family, Llama, Mistral, and Claude
are all decoder-only models. In a decoder-only Transformer, the
self-attention is "causal" or "masked" -- each token can only attend to
itself and preceding tokens, never to future tokens. This makes the
architecture naturally suited for autoregressive generation: the model
predicts one token at a time, and each new token is appended to the
sequence for the next prediction step.

Decoder-only architectures have proven more efficient and scalable than
encoder-decoder designs for general-purpose language modeling. They use
all parameters for both understanding and generation, whereas
encoder-decoder models split capacity between the two functions. The
trade-off is that decoder-only models have no separate encoder to
condition on long input contexts, though modern context windows (128K
tokens in GPT-4 Turbo, 200K in Claude, 1M+ in Gemini) have largely
obsoleted this concern.

### Training: Pre-training, Fine-tuning, and Alignment

LLM training proceeds in stages. Pre-training is the most
computationally expensive phase: the model is trained on a massive corpus
of text -- typically web pages, books, academic papers, and code
repositories -- using a simple language modeling objective. For each
position in each document, the model predicts the next token given all
previous tokens, and the error between its prediction and the actual next
token is backpropagated to update the weights. GPT-3 was trained on
approximately 300 billion tokens; Llama 3 was trained on over 15
trillion tokens. Pre-training costs for frontier models now run into the
hundreds of millions of dollars.

After pre-training, the model undergoes supervised fine-tuning (SFT):
it is trained on curated datasets of instruction-response pairs,
teaching it to follow instructions rather than simply continue text.
This produces a model that can engage in dialogue, answer questions, and
follow complex directives.

The final stage is alignment, typically using Reinforcement Learning
from Human Feedback (RLHF) or its variants. Human raters compare
multiple model outputs for the same prompt and indicate which they
prefer. A reward model is trained on these preferences, and the LLM is
fine-tuned using reinforcement learning to maximize the reward model's
score. Alternatives like Direct Preference Optimization (DPO) simplify
this by directly optimizing on preference pairs without a separate
reward model. Alignment makes models more helpful, harmless, and honest
-- reducing hallucination, refusal of harmful requests, and undesirable
behaviors.

### Mixture of Experts (MoE)

A key architectural innovation that emerged from scaling research is
Mixture of Experts. In a dense Transformer, every parameter is used for
every input token. In an MoE model, the feed-forward layers are replaced
with multiple "expert" subnetworks, and a learned routing mechanism
selects a subset of experts (typically 2 out of 8 or more) to process
each token. This means the model has many more total parameters than a
dense model of equivalent compute cost, but only a fraction are active
for any given input.

Mixture of Experts allows models to scale total parameter count
dramatically without proportionally increasing inference cost. GPT-4 is
widely believed to use an MoE architecture with 8 experts and
approximately 1.8 trillion total parameters. Mistral's Mixtral models
demonstrated that MoE could be applied at smaller scales with strong
results. Wang et al. (2024) confirmed that power-law scaling frameworks
apply to MoE models and that they achieve lower test loss than dense
models at equivalent compute budgets.

### Tokenization

Before text reaches the Transformer, it must be converted to tokens. A
tokenizer breaks text into discrete units and maps each to an integer
ID. Modern LLMs use subword tokenization, typically Byte-Pair Encoding
(BPE), which strikes a balance between word-level and character-level
representations. Common words become single tokens ("the" = token 262),
while rare words are split into subword pieces ("transformer" might be
["transform", "er"]). The tokenizer's vocabulary size is typically
30,000 to 100,000 tokens.

Tokenization is a surprisingly consequential design choice. It
determines how many tokens are needed to represent a given text (and
therefore the computational cost), how the model handles multilingual
text, code, and numbers, and even affects reasoning capabilities. Poor
tokenization of numbers, for example, can prevent a model from learning
basic arithmetic. Recent research (Mayilvahanan et al., 2025) has shown
that the pretraining data and tokenizer determine the fundamental scaling
trend, while model architecture and size have limited impact on
loss-to-loss scaling relationships.

### Scaling Laws

Scaling laws are empirical regularities discovered by Kaplan et al.
(2020) at OpenAI: for a given increase in compute, there is a predictable
reduction in language modeling loss that follows a power law. The
original Kaplan scaling laws suggested that model size should be scaled
more aggressively than dataset size. The Chinchilla laws (Hoffmann et
al., 2022) corrected this, finding the optimal ratio is roughly 20
training tokens per parameter -- meaning many models were undertrained.

Scaling laws are not merely academic curiosities. They are the primary
planning tool for frontier AI labs. Before committing hundreds of
millions of dollars to train a model, labs use scaling laws fitted to
smaller experimental runs to predict the performance of the full-scale
model. MIT-IBM Watson AI Lab research (2025) systematically evaluated
over 1,000 scaling law formulations across 40 model families and 485
models, finding that scaling laws can predict large model performance
with median errors as low as 3-5% when fitted properly on related models.

A critical open question is whether scaling laws will continue to hold.
There are signs of diminishing returns at the frontier: incremental
gains from scaling are becoming more expensive, and some researchers
argue that we are approaching the limits of available high-quality
training data. The "wall" hypothesis suggests that the supply of new,
high-quality text on the internet is finite and models are already
consuming it faster than it is being produced. Synthetic data --
generated by other models -- is increasingly used to augment training
sets, but carries risks of amplifying errors and reducing diversity.

## Capabilities and Emergent Abilities

One of the most striking and consequential properties of LLMs is the
emergence of capabilities that were not explicitly programmed or trained
for. Wei et al. (2022) documented that as models scale past certain size
thresholds, they acquire qualitatively new abilities: arithmetic,
translation between languages they were never explicitly trained to
translate between, multi-step reasoning, and the ability to follow
instructions explained in natural language rather than demonstrated
through examples.

The standard explanation for emergence draws on phase transitions in
complex systems. Below a critical threshold of scale, the model simply
lacks the capacity to represent the patterns needed for a task. As
parameters and data increase, a qualitative shift occurs when the model
has enough capacity to encode the relevant regularities. The resulting
behavior appears sudden because the evaluation metrics used --
especially accuracy on discrete tasks -- are nonlinear. Schaeffer et al.
(2023) argued that when continuous metrics are used instead of
accuracy-based ones, emergence looks smoother, and some "emergent"
abilities may be artifacts of the chosen metric. The debate is not
settled: while some capabilities are genuinely emergent from a
functional perspective (the model could not do X at size N but can at
size 2N), the underlying loss landscape may improve more continuously.

Practically important emergent capabilities include:

- **In-context learning:** The ability to perform a task from a few
  examples provided in the prompt, without any weight updates. GPT-3
  demonstrated this at scale, and it is now a standard evaluation
  paradigm.
- **Chain-of-thought reasoning:** When prompted to "think step by step,"
  LLMs produce intermediate reasoning steps that dramatically improve
  accuracy on multi-step problems. This was shown to be effective by Wei
  et al. (2022) and has become a standard prompting technique.
- **Tool use and code execution:** Frontier models can write and execute
  code, call APIs, and use external tools to augment their capabilities.
  This bridges the gap between pure language modeling and agentic
  behavior.
- **Theory of mind and social reasoning:** LLMs show evidence of being
  able to model other agents' beliefs, intentions, and knowledge states,
  though the extent and robustness of this capability is debated.

Current frontier models -- GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro,
and Llama 3.1 405B -- achieve scores of 85-90% on MMLU (a benchmark
spanning 57 academic subjects), above 90% on HumanEval (Python code
generation), and above 90% on GSM8K (grade-school math). Performance
gaps between the top models are narrowing, and competitive pressure is
driving rapid iteration cycles measured in months rather than years.

## Evidence

The empirical case for LLMs rests on three pillars: scaling law
predictability, benchmark performance, and real-world deployment impact.

Kaplan et al. (2020) demonstrated that language model loss follows
predictable power-law scaling across six orders of magnitude in compute.
They trained models ranging from 768 parameters to 1.5 billion
parameters and found that test loss decreased smoothly with increased
compute, model size, and data size, with no signs of deviation from the
trend. This work established that performance improvements from scaling
were not a one-off fluke but a reliable, mathematically characterizable
phenomenon.

Hoffmann et al. (2022) refined the scaling picture by training over 400
models from 70 million to 16 billion parameters, systematically varying
model size and training tokens. They confirmed the power-law
relationship and identified the compute-optimal frontier. Their
Chinchilla model (70B parameters, 1.4T training tokens) achieved an
MMLU score of 67.5%, outperforming Gopher (280B parameters, 300B tokens)
at 60.0%, despite having one-quarter the parameters. This directly
demonstrated that training data volume was being systematically
underinvested.

On benchmark performance, the trajectory is unambiguous. GPT-2 (2019,
1.5B parameters) scored 63.7% on the LAMBADA language understanding
task. GPT-3 (2020, 175B) reached 86.4%. GPT-4 (2023) scored in the 90th
percentile on the Uniform Bar Exam (297/400) and the 93rd percentile on
the SAT Evidence-Based Reading and Writing section. By 2025, frontier
models were approaching or exceeding human-level performance on
professional and academic benchmarks including the USMLE medical
licensing exam and the LSAT, while simultaneously handling multimodal
inputs (images, audio, video) that earlier models could not process.

The Chinchilla scaling laws have been replicated and extended across
model families. Wang et al. (2024) confirmed that power-law scaling
holds for Mixture of Experts architectures, with MoE models achieving
lower test loss at equivalent training compute compared to dense models.
The MIT-IBM Watson AI Lab (2025) analyzed 485 models across 40 families
and found that scaling laws fitted to smaller models predict larger model
performance with median errors of 3-5%, providing strong evidence that
the scaling paradigm remains a reliable engineering tool.

The most visible evidence comes from deployment. ChatGPT reached 100
million users within two months of launch -- the fastest consumer
application adoption in history. GitHub Copilot is used by over one
million developers and generates a substantial fraction of new code on
the platform. LLMs are being deployed in medicine (clinical note
summarization, radiology report analysis, drug discovery), law (contract
review, e-discovery, legal research), education (personalized tutoring,
essay feedback), and scientific research (literature review,
hypothesis generation, protein structure prediction). These deployments
provide continuous, real-world evidence of capability that no benchmark
can fully capture.

## Implications

The trajectory of LLM capability has immediate implications for
software engineering, the economics of knowledge work, and the structure
of AI research itself.

For software engineering, LLMs are reshaping how code is written.
Copilot and similar tools have moved from novelty to necessity for
many developers, handling boilerplate, documentation, test generation,
and increasingly complex algorithmic tasks. The SWE-bench benchmark,
which measures LLM performance on real GitHub issues, has seen scores
rise from near zero to approximately 49% in two years. The economic
implication is a step-change in developer productivity that may rival
the effects of high-level languages, version control, and the internet
on software development velocity.

For knowledge work more broadly, LLMs act as a force multiplier for
tasks involving text synthesis, summarization, analysis, and
translation. The marginal cost of producing a competent first draft --
of a legal brief, a market analysis, a research summary, or a grant
proposal -- is collapsing toward zero. This does not eliminate the need
for expertise (review, verification, and contextual judgment remain
essential), but it shifts the bottleneck from production to evaluation.
Knowledge workers who master LLM-assisted workflows will have an
asymmetric productivity advantage over those who do not.

The capital intensity of frontier model training is creating a
concentration dynamic. Pre-training runs now cost hundreds of millions
of dollars, and each successive generation roughly doubles in cost.
This creates high barriers to entry and concentrates frontier
capability in a small number of well-capitalized organizations: OpenAI
(backed by Microsoft), Anthropic (backed by Amazon and Google), Google
DeepMind, and Meta (which open-sources its models). The open-source
ecosystem (Llama, Mistral, Qwen, DeepSeek) is narrowing the gap, but
the frontier remains expensive to reach.

The data wall problem may force a change in the scaling paradigm.
High-quality text data is a finite resource, and models are consuming
it rapidly. Synthetic data generation -- using existing models to
generate training data for future models -- is increasingly common, but
risks model collapse (degradation from training on model-generated
rather than human-generated data). Multimodal training (incorporating
images, video, and audio alongside text) and reinforcement learning
approaches that generate their own training signal (like DeepMind's
AlphaZero for games) are potential paths around the data wall, but
neither is proven at scale for general-purpose language models.

The agentic turn -- models that do not just respond to prompts but
pursue goals, use tools, and act autonomously -- represents the next
frontier. OpenAI's o-series models, Anthropic's computer use
capabilities, and the rapid development of agent frameworks point
toward LLMs becoming the reasoning core of semi-autonomous software
systems. This raises the stakes: a model that merely generates text
can be filtered for safety; a model that can execute code, browse the
web, and interact with APIs has a much larger surface area for both
beneficial and harmful actions.

## Sources

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L.,
   Gomez, A.N., Kaiser, L., & Polosukhin, I. (2017). "Attention Is All
   You Need." Advances in Neural Information Processing Systems 30
   (NIPS 2017). https://arxiv.org/abs/1706.03762 [high]

2. Brown, T., Mann, B., Ryder, N., et al. (2020). "Language Models are
   Few-Shot Learners." NeurIPS 2020. https://arxiv.org/abs/2005.14165
   [high]

3. Kaplan, J., McCandlish, S., Henighan, T., Brown, T.B., Chess, B.,
   Child, R., Gray, S., Radford, A., Wu, J., & Amodei, D. (2020).
   "Scaling Laws for Neural Language Models." arXiv:2001.08361.
   https://arxiv.org/abs/2001.08361 [high]

4. Hoffmann, J., Borgeaud, S., Mensch, A., et al. (2022). "Training
   Compute-Optimal Large Language Models." arXiv:2203.15556.
   https://arxiv.org/abs/2203.15556 [high]

5. Wei, J., Tay, Y., Bommasani, R., et al. (2022). "Emergent Abilities
   of Large Language Models." Transactions on Machine Learning Research
   (TMLR). https://arxiv.org/abs/2206.07682 [high]

6. Schaeffer, R., Miranda, B., & Koyejo, S. (2023). "Are Emergent
   Abilities of Large Language Models a Mirage?" NeurIPS 2023.
   https://arxiv.org/abs/2304.15004 [high]

7. Wang, S., Chen, Z., Li, B., He, K., Zhang, M., & Wang, J. (2024).
   "Scaling Laws Across Model Architectures: A Comparative Analysis of
   Dense and MoE Models in Large Language Models." EMNLP 2024.
   https://aclanthology.org/2024.emnlp-main.319/ [high]

8. DataStudios (2025). "ChatGPT vs. Google Gemini vs. Anthropic Claude:
   Full Report and Comparison (Mid-2025)."
   https://www.datastudios.org/post/chatgpt-vs-google-gemini-vs-anthropic-claude-full-report-and-comparison-mid-2025
   [medium]

9. MIT News (2025). "How to build AI scaling laws for efficient LLM
   training and budget maximization."
   https://news.mit.edu/2025/how-build-ai-scaling-laws-efficient-llm-training-budget-maximization-0916
   [medium]

## See Also

- `library/coding-agentic-ai/agent-skill-systems.md` -- how LLMs serve
  as the reasoning engine for modular agent architectures.
- `library/coding-agentic-ai/multi-agent-orchestration.md` -- multi-agent
  systems that depend on LLM capabilities for coordination and
  delegation.
- `library/coding-agentic-ai/context-window-management.md` -- techniques
  for managing the constrained context windows within which LLMs
  operate.
- `library/science/evolution-by-natural-selection.md` -- the parallel
  between emergent abilities in LLMs and emergent complexity in
  biological evolution.
