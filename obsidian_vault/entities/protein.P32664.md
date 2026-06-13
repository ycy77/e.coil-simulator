---
entity_id: "protein.P32664"
entity_type: "protein"
name: "nudC"
source_database: "UniProt"
source_id: "P32664"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nudC yjaD b3996 JW5548"
---

# nudC

`protein.P32664`

## Static

- Type: `protein`
- Source: `UniProt:P32664`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: mRNA decapping enzyme that specifically removes the nicotinamide adenine dinucleotide (NAD) cap from a subset of mRNAs by hydrolyzing the diphosphate linkage to produce nicotinamide mononucleotide (NMN) and 5' monophosphate mRNA (PubMed:25533955, PubMed:27428510, PubMed:27561816). The NAD-cap is present at the 5'-end of some mRNAs and stabilizes RNA against 5'-processing (PubMed:25533955). Has preference for mRNAs with a 5'-end purine (PubMed:27428510). Catalyzes the hydrolysis of a broad range of dinucleotide pyrophosphates, but uniquely prefers the reduced form of NADH (PubMed:25533955, PubMed:7829480). {ECO:0000269|PubMed:25533955, ECO:0000269|PubMed:27428510, ECO:0000269|PubMed:27561816, ECO:0000269|PubMed:7829480}.

## Biological Role

Catalyzes NAD+ phosphohydrolase (reaction.R00103). Component of RNA decapping hydrolase (complex.ecocyc.CPLX0-7974).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco04146` Peroxisome (KEGG)

## Annotation

FUNCTION: mRNA decapping enzyme that specifically removes the nicotinamide adenine dinucleotide (NAD) cap from a subset of mRNAs by hydrolyzing the diphosphate linkage to produce nicotinamide mononucleotide (NMN) and 5' monophosphate mRNA (PubMed:25533955, PubMed:27428510, PubMed:27561816). The NAD-cap is present at the 5'-end of some mRNAs and stabilizes RNA against 5'-processing (PubMed:25533955). Has preference for mRNAs with a 5'-end purine (PubMed:27428510). Catalyzes the hydrolysis of a broad range of dinucleotide pyrophosphates, but uniquely prefers the reduced form of NADH (PubMed:25533955, PubMed:7829480). {ECO:0000269|PubMed:25533955, ECO:0000269|PubMed:27428510, ECO:0000269|PubMed:27561816, ECO:0000269|PubMed:7829480}.

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco04146` Peroxisome (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00103|reaction.R00103]] `KEGG` `database` - via EC:3.6.1.22
- `is_component_of` --> [[complex.ecocyc.CPLX0-7974|complex.ecocyc.CPLX0-7974]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3996|gene.b3996]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32664`
- `KEGG:ecj:JW5548;eco:b3996;ecoc:C3026_21585;`
- `GeneID:93777898;948498;`
- `GO:GO:0000210; GO:0000287; GO:0006402; GO:0006742; GO:0008270; GO:0019677; GO:0030145; GO:0035529; GO:0042803; GO:0048255; GO:0110153; GO:0110155`
- `EC:3.6.1.-; 3.6.1.22`

## Notes

NAD-capped RNA hydrolase NudC (DeNADding enzyme NudC) (EC 3.6.1.-) (NADH pyrophosphatase) (EC 3.6.1.22)
