---
entity_id: "complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX"
entity_type: "complex"
name: "xanthosine phosphorylase"
source_database: "EcoCyc"
source_id: "XANTHOSINEPHOSPHORY-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "purine nucleoside phosphorylase II"
---

# xanthosine phosphorylase

`complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:XANTHOSINEPHOSPHORY-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P45563|protein.P45563]]

## Enriched Summary

Xanthosine phosphorylase (XapA or PNP-II) is one of two purine nucleoside phosphorylases (PNPs) in E. coli. PNPs use orthophosphate to cleave the N-glycosidic bond of the β-(deoxy)ribonucleosides to produce α-(deoxy)ribose1-phosphate and the free purine base. The bases can be utilized as precursors in the synthesis of nucleotides in the purine salvage pathways, as well as a nitrogen source. The pentose-1-phosphate formed serves as a carbon source. The other PNP, PNP-I DEOD-CPLX, differs in substrate specificity. XapA does not cleave or synthesize adenosine and deoxyadenosine but catalyzes the phosphorolysis of xanthosine, inosine and guanosine with comparable efficiency. Therefore, this enzyme has been variously referred to as xanthosine phosphorylase and inosine-guanosine phosphorylase . XapA enables E. coli to grow on xanthosine as the sole source of carbon . The amino acid sequence of XapA resembles that of mammalian purine nucleoside phosphorylases and has no similarity with PNP-I . Recently, an investigation of the NAD+ salvage pathway showed that a ΔnadC ΔpncA double mutant can grow slowly in M9 minimal medium containing nicotinamide (NAM). This implied the presence of a previously undefined activity that routes NAM into NAD+ synthesis...

## Biological Role

Catalyzes INOPHOSPHOR-RXN (reaction.ecocyc.INOPHOSPHOR-RXN), RXN0-5199 (reaction.ecocyc.RXN0-5199), RXN0-7092 (reaction.ecocyc.RXN0-7092), XANTHOSINEPHOSPHORY-RXN (reaction.ecocyc.XANTHOSINEPHOSPHORY-RXN).

## Annotation

Xanthosine phosphorylase (XapA or PNP-II) is one of two purine nucleoside phosphorylases (PNPs) in E. coli. PNPs use orthophosphate to cleave the N-glycosidic bond of the β-(deoxy)ribonucleosides to produce α-(deoxy)ribose1-phosphate and the free purine base. The bases can be utilized as precursors in the synthesis of nucleotides in the purine salvage pathways, as well as a nitrogen source. The pentose-1-phosphate formed serves as a carbon source. The other PNP, PNP-I DEOD-CPLX, differs in substrate specificity. XapA does not cleave or synthesize adenosine and deoxyadenosine but catalyzes the phosphorolysis of xanthosine, inosine and guanosine with comparable efficiency. Therefore, this enzyme has been variously referred to as xanthosine phosphorylase and inosine-guanosine phosphorylase . XapA enables E. coli to grow on xanthosine as the sole source of carbon . The amino acid sequence of XapA resembles that of mammalian purine nucleoside phosphorylases and has no similarity with PNP-I . Recently, an investigation of the NAD+ salvage pathway showed that a ΔnadC ΔpncA double mutant can grow slowly in M9 minimal medium containing nicotinamide (NAM). This implied the presence of a previously undefined activity that routes NAM into NAD+ synthesis. An additional mutation in xapA further decreased growth of the ΔnadC ΔpncA mutant on NAM, and purified XapA was shown to catalyze formation of nicotinamide riboside from nicotinamide at low efficiency. Additional experiments with deletion mutations involving nadR indicate that XapA may also be involved in PWY3O-4106 . XapA predominantly exists as a hexamer with some evidence for co-existence of a trimeric from . Crystal structures of XapA were solved in the presence of guanine and phosphate as well as xanthine and sulfate. XapA for

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.INOPHOSPHOR-RXN|reaction.ecocyc.INOPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5199|reaction.ecocyc.RXN0-5199]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7092|reaction.ecocyc.RXN0-7092]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.XANTHOSINEPHOSPHORY-RXN|reaction.ecocyc.XANTHOSINEPHOSPHORY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P45563|protein.P45563]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:XANTHOSINEPHOSPHORY-CPLX`
- `QSPROTEOME:QS00183317`

## Notes

6*protein.P45563
