---
entity_id: "protein.P68739"
entity_type: "protein"
name: "nfi"
source_database: "UniProt"
source_id: "P68739"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nfi yjaF b3998 JW5547"
---

# nfi

`protein.P68739`

## Static

- Type: `protein`
- Source: `UniProt:P68739`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: DNA repair enzyme involved in the repair of deaminated bases. Selectively cleaves double-stranded DNA at the second phosphodiester bond 3' to a deoxyinosine leaving behind the intact lesion on the nicked DNA. Has a wide substrate spectrum. In addition to deoxyinosine-containing DNA, the enzyme cleaves DNA containing urea residues, AP sites, base mismatches, insertion/deletion mismatches, flaps, and pseudo-Y structures. Participates in the excision repair of hypoxanthine and xanthine (deaminated adenine and guanine) in DNA. It thereby reduces the mutagenic effects of nitrous acid by attacking lesions caused by nitrosative deamination. Also active on inosines in single- and double-stranded RNA. May cleave tRNA(Arg2), which contains inosine at the wobble position. {ECO:0000255|HAMAP-Rule:MF_00801, ECO:0000269|PubMed:11104906, ECO:0000269|PubMed:23912683, ECO:0000269|PubMed:6246346, ECO:0000269|PubMed:8206931, ECO:0000269|PubMed:9388217}. nfi encodes Endonuclease V, a DNA repair enzyme which catalyses the initiating reaction in an alternate excision repair (AER) pathway that targets a variety of DNA lesions including the purine deamination products, deoxyinosine and deoxyxanthosine...

## Biological Role

Catalyzes RXN-21350 (reaction.ecocyc.RXN-21350). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: DNA repair enzyme involved in the repair of deaminated bases. Selectively cleaves double-stranded DNA at the second phosphodiester bond 3' to a deoxyinosine leaving behind the intact lesion on the nicked DNA. Has a wide substrate spectrum. In addition to deoxyinosine-containing DNA, the enzyme cleaves DNA containing urea residues, AP sites, base mismatches, insertion/deletion mismatches, flaps, and pseudo-Y structures. Participates in the excision repair of hypoxanthine and xanthine (deaminated adenine and guanine) in DNA. It thereby reduces the mutagenic effects of nitrous acid by attacking lesions caused by nitrosative deamination. Also active on inosines in single- and double-stranded RNA. May cleave tRNA(Arg2), which contains inosine at the wobble position. {ECO:0000255|HAMAP-Rule:MF_00801, ECO:0000269|PubMed:11104906, ECO:0000269|PubMed:23912683, ECO:0000269|PubMed:6246346, ECO:0000269|PubMed:8206931, ECO:0000269|PubMed:9388217}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-21350|reaction.ecocyc.RXN-21350]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3998|gene.b3998]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P68739`
- `KEGG:ecj:JW5547;eco:b3998;ecoc:C3026_21595;`
- `GeneID:75169444;948502;`
- `GO:GO:0000287; GO:0003727; GO:0005829; GO:0006281; GO:0016891; GO:0043737`
- `EC:3.1.21.7`

## Notes

Endonuclease V (EndoV) (EC 3.1.21.7) (Deoxyinosine 3'endonuclease) (Deoxyribonuclease V) (DNase V)
