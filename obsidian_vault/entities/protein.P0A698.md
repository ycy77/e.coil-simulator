---
entity_id: "protein.P0A698"
entity_type: "protein"
name: "uvrA"
source_database: "UniProt"
source_id: "P0A698"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00205}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uvrA dinE b4058 JW4019"
---

# uvrA

`protein.P0A698`

## Static

- Type: `protein`
- Source: `UniProt:P0A698`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00205}.

## Enriched Summary

FUNCTION: The UvrABC repair system catalyzes the recognition and processing of DNA lesions. UvrA is an ATPase and a DNA-binding protein. A damage recognition complex composed of 2 UvrA and 2 UvrB subunits scans DNA for abnormalities. When the presence of a lesion has been verified by UvrB, the UvrA molecules dissociate. {ECO:0000255|HAMAP-Rule:MF_00205}. uvrA encodes one of the three key proteins of the nucleotide excision repair (NER) pathway. UvrA forms homodimers in the presence of ATP , and at physiological concentrations UvrA associaties with UvrB to form a UvrA2B complex in an ATP-dependent interaction . UvrA binds DNA as a dimer with a strong preference for DNA ends . uvrA insertion mutants were identified in a genetic screen for genes that are important for survival of exposure to ionizing radiation (IR). A uvrA deletion mutant has a substantial decrease in IR survival . Deletion of uvrA results in a significant decrease in persister fraction following fluoroquinolone treatment; the absence of uvrA impedes persister awakening .

## Biological Role

Component of excision nuclease UvrABC (complex.ecocyc.UVRABC-CPLX).

## Enriched Pathways

- `eco03420` Nucleotide excision repair (KEGG)

## Annotation

FUNCTION: The UvrABC repair system catalyzes the recognition and processing of DNA lesions. UvrA is an ATPase and a DNA-binding protein. A damage recognition complex composed of 2 UvrA and 2 UvrB subunits scans DNA for abnormalities. When the presence of a lesion has been verified by UvrB, the UvrA molecules dissociate. {ECO:0000255|HAMAP-Rule:MF_00205}.

## Pathways

- `eco03420` Nucleotide excision repair (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.UVRABC-CPLX|complex.ecocyc.UVRABC-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4058|gene.b4058]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A698`
- `KEGG:ecj:JW4019;eco:b4058;ecoc:C3026_21930;`
- `GeneID:93777773;948559;`
- `GO:GO:0000715; GO:0003677; GO:0005524; GO:0005829; GO:0006281; GO:0006289; GO:0006294; GO:0006974; GO:0008270; GO:0009314; GO:0009380; GO:0009381; GO:0009432; GO:0016887; GO:0042802; GO:1990391`

## Notes

UvrABC system protein A (UvrA protein) (Excinuclease ABC subunit A)
