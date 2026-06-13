---
entity_id: "protein.P0AFN2"
entity_type: "protein"
name: "pspC"
source_database: "UniProt"
source_id: "P0AFN2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pspC b1306 JW1299"
---

# pspC

`protein.P0AFN2`

## Static

- Type: `protein`
- Source: `UniProt:P0AFN2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: The phage shock protein (psp) operon (pspABCDE) may play a significant role in the competition for survival under nutrient- or energy-limited conditions. PspC is involved in transcription regulation. {ECO:0000269|PubMed:1712397}. PspC is a positive regulator of the TU00326 operon expression . EG10777-MONOMER PspB and PspC together act to activate expression of the psp operon in response to infection with bacteriophage, exposure to ethanol, osmotic shock, and heat shock; PspC is essential for this activation, whereas PspB is not strictly required . PspC appears to be required for PspB to interact with PspA . PspC is also reported as the toxin of a potential PspC-PspB toxin-antitoxin pair . The intramembrane protease FtsH destabilizes PspC . PspC is an inner membrane protein that is proposed to consist of an N-terminal cytoplasmic domain, a central transmembrane domain (residues 40-68), and a C-terminal periplasmic domain with a leucine zipper motif . A conserved glycine residue at position 48 is required for PspC function. It has been proposed that stress induces a topology switch whereby the C-terminal domain becomes cytoplasmic, thus enabling its interaction with EG10776-MONOMER PspA . Early results suggested the existence of a PspC dimer that resists dissociation in the presence of SDS...

## Biological Role

Component of PspABC complex (complex.ecocyc.CPLX0-10367).

## Annotation

FUNCTION: The phage shock protein (psp) operon (pspABCDE) may play a significant role in the competition for survival under nutrient- or energy-limited conditions. PspC is involved in transcription regulation. {ECO:0000269|PubMed:1712397}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10367|complex.ecocyc.CPLX0-10367]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1306|gene.b1306]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFN2`
- `KEGG:ecj:JW1299;eco:b1306;ecoc:C3026_07660;`
- `GeneID:93775432;945499;`
- `GO:GO:0005886; GO:0010557; GO:0080135`

## Notes

Phage shock protein C
