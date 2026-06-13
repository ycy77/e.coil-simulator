---
entity_id: "protein.P0A6Z3"
entity_type: "protein"
name: "htpG"
source_database: "UniProt"
source_id: "P0A6Z3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16079137}. Cell inner membrane {ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "htpG b0473 JW0462"
---

# htpG

`protein.P0A6Z3`

## Static

- Type: `protein`
- Source: `UniProt:P0A6Z3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16079137}. Cell inner membrane {ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Molecular chaperone. Has ATPase activity. HtpG is a member of the Hsp90 (heat shock protein, 90kDa) family of molecular chaperones . Purified HtpG is an ATPase (with a kcat of 0.011 sec-1 and a KM for ATP of 250 µM ). Purified, immobilised HtpG binds the heat shock alternative sigma factor σ32 and an unidentified cyclophilin (peptidyl-prolyl isomerase) . HtpG participates in the folding of newly synthesized proteins under mild heat shock conditions ; purified HtpG suppresses the thermal aggregation of citrate synthase at 43°C (see also ). HtpG collaborates with the EG10241-MONOMER "DnaK" chaperone system to reactivate inactive protein substrates; the ATPase activity of HtpG is essential for this activity; HtpG and DnaK physically interact in vivo and in vitro (see further ). HtpG binds partially folded states of a model substrate (Staphylococcal nuclease) that are transiently sampled from its thermodynamically stable native state . HtpG is a phosphoprotein in vivo ; the purified protein acquires 1.5 phosphate groups/molecule predominantly on serine and threonine residues but also on a His residue . Purified HtpG is a dimer in solution but oligomerizes at higher temperatures (65°C) . The oligomeric state and activity of the protein is affected by the presence of divalent cations in vitro...

## Biological Role

Component of chaperone protein HtpG (complex.ecocyc.CPLX0-2641).

## Annotation

FUNCTION: Molecular chaperone. Has ATPase activity.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2641|complex.ecocyc.CPLX0-2641]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0473|gene.b0473]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6Z3`
- `KEGG:ecj:JW0462;eco:b0473;ecoc:C3026_02325;`
- `GeneID:86863018;93776977;945099;`
- `GO:GO:0005524; GO:0005829; GO:0005886; GO:0006457; GO:0006974; GO:0009408; GO:0016887; GO:0042802; GO:0042803; GO:0043093; GO:0044183; GO:0051082; GO:0051087; GO:0140662`

## Notes

Chaperone protein HtpG (Heat shock protein C62.5) (Heat shock protein HtpG) (High temperature protein G)
