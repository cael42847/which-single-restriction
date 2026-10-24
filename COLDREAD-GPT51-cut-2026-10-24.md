# GPT-5.1 (OpenRouter, model openai/gpt-5.1, provider OpenAI) cold read of Which-Single-Restriction-2026-10-24.pdf pp.1-9, sha256 0ba981937db81d74…; sent 17:50:00, back 17:50:05; key usage 117.4933 -> 117.4933 USD; tokens {'prompt_tokens': 6997, 'completion_tokens': 607, 'total_tokens': 7604, 'cost': 0.01481625, 'is_byok': False, 'prompt_tokens_details': {'cached_tokens': 0, 'cache_write_tokens': 0, 'audio_tokens': 0, 'video_tokens': 0}, 'cost_details': {'upstream_inference_cost': 0.01481625, 'upstream_inference_prompt_cost': 0.00874625, 'upstream_inference_completions_cost': 0.00607}, 'completion_tokens_details': {'reasoning_tokens': 0, 'image_tokens': 0, 'audio_tokens': 0}}. Question verbatim: "List only statements a reviewer would find wrong, unsupported or self-contradictory, with page and quote. No style notes." Answer verbatim below.

Page 1  
- “Which single restriction removes the most collusion at the least cost, in a two-seller LLM market?”  
  – Not supported as stated: later (pp. 7–8, Figure 3 and Discussion) the arithmetic rival is acknowledged as removing more collusion, with the patrol preferred only under an extra criterion (“among measures that leave the sellers in charge”), so the opening “single restriction” claim is overstated without that qualifier.  

Page 1  
- “The intervention that removed the most is the one avalanche services call artificial triggering.”  
  – Contradicted by later text: on p. 7 it is stated that “The arithmetic rival removes the most (0.95 to 0.99 on Haiku, 0.88 to 0.99 on DeepSeek) but replaces a seller”, so the patrol is not actually the intervention that “removed the most” collusion overall.  

Page 1  
- “DeepSeek v4.1 flash from 1.79 to 1.45, just under competitive 1.473.”  
  – Internally inconsistent numerically: 1.45 is not “just under” 1.473 but noticeably lower; the language suggests proximity that is not borne out by the numbers (difference 0.023 ≈ 1.6% of the competitive price).  

Page 4  
- “It costs four forced prices in 100, and makes markets predictable: spread fell to about two fifths or less.”  
  – Not adequately supported in that context: later detailed numbers (p. 5) give specific sd reductions (e.g. 0.31 to 0.12 and 0.22 to 0.08), which are around 0.39 and 0.36 of the original spread, but no general argument or statistic is given that this “two fifths or less” holds across all relevant market conditions, especially other μ values.  

Page 8  
- “Among measures that leave the sellers in charge, the undercutting sentence comes close to the patrol on price (it removed 0.81 on Haiku, between the 10% cut's 0.69 and the 20% cut's 0.89; 0.97 on DeepSeek, level with the 10% cut's 1.07).”  
  – Self-contradictory / unclear normalization: claiming the undercutting sentence on DeepSeek removed 0.97 collusion while the 10% cut removed 1.07 implies the 10% cut removes more than 100% of baseline collusion, which conflicts with the earlier definition of “collusion removed” as a fraction between 0 and 1 (from competitive to cartel). No explanation is given for values above 1, so the comparative and the scale are not coherently defined.