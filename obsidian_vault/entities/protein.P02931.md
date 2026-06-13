---
entity_id: "protein.P02931"
entity_type: "protein"
name: "ompF"
source_database: "UniProt"
source_id: "P02931"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:2464593}; Multi-pass membrane protein {ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ompF cmlB coa cry tolF b0929 JW0912"
---

# ompF

`protein.P02931`

## Static

- Type: `protein`
- Source: `UniProt:P02931`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:2464593}; Multi-pass membrane protein {ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Forms pores that allow passive diffusion of small molecules across the outer membrane. {ECO:0000305|PubMed:19721064}.; FUNCTION: (Microbial infection) It is also a receptor for the bacteriophage T2. Is the major receptor for colicin E5 (Probable). {ECO:0000305|PubMed:27723824}.; FUNCTION: (Microbial infection) Probably translocates colicin E3 (and other A-type colicins) across the outer membrane (PubMed:18636093). {ECO:0000269|PubMed:18636093}.; FUNCTION: (Microbial infection) A mixed OmpC-OmpF heterotrimer is the outer membrane receptor for toxin CdiA-EC536 (ECL_04451); polymorphisms in extracellular loops 4 and 5 of OmpC confer susceptibility to CdiA-EC536-mediated toxicity. {ECO:0000269|PubMed:27723824}. OmpF is a general outer membrane (OM) porin which mediates the non-specific diffusion of small solutes such as sugars, ions and amino acids. The major non-specific OM porins of E. coli K-12 (OmpF and CPLX0-7533 "OmpC") are typically defined by an exclusion limit based on substrate mass (~600 daltons) but there are large differences in penetration rates within solutes due to factors such as size, hydrophobicity and charge (discussed in ). OmpF acts as a phage receptor (see for example ) and is required for the activity of various colicins (see for example )...

## Biological Role

Component of outer membrane porin F (complex.ecocyc.CPLX0-7534).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Forms pores that allow passive diffusion of small molecules across the outer membrane. {ECO:0000305|PubMed:19721064}.; FUNCTION: (Microbial infection) It is also a receptor for the bacteriophage T2. Is the major receptor for colicin E5 (Probable). {ECO:0000305|PubMed:27723824}.; FUNCTION: (Microbial infection) Probably translocates colicin E3 (and other A-type colicins) across the outer membrane (PubMed:18636093). {ECO:0000269|PubMed:18636093}.; FUNCTION: (Microbial infection) A mixed OmpC-OmpF heterotrimer is the outer membrane receptor for toxin CdiA-EC536 (ECL_04451); polymorphisms in extracellular loops 4 and 5 of OmpC confer susceptibility to CdiA-EC536-mediated toxicity. {ECO:0000269|PubMed:27723824}.

## Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7534|complex.ecocyc.CPLX0-7534]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0929|gene.b0929]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P02931`
- `KEGG:ecj:JW0912;eco:b0929;ecoc:C3026_05710;`
- `GeneID:75204020;945554;`
- `GO:GO:0001530; GO:0005216; GO:0008289; GO:0009279; GO:0015031; GO:0015288; GO:0016020; GO:0034220; GO:0034702; GO:0042802; GO:0042912; GO:0046930; GO:0070207; GO:0097718`

## Notes

Outer membrane porin F (Outer membrane protein 1A) (Outer membrane protein B) (Outer membrane protein F) (Outer membrane protein IA) (Porin OmpF)
