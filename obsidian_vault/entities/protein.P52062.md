---
entity_id: "protein.P52062"
entity_type: "protein"
name: "hemW"
source_database: "UniProt"
source_id: "P52062"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:29282292}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hemW yggW b2955 JW2922"
---

# hemW

`protein.P52062`

## Static

- Type: `protein`
- Source: `UniProt:P52062`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:29282292}.

## Enriched Summary

FUNCTION: Probably acts as a heme chaperone, transferring heme to the NarI subunit of the respiratory enzyme nitrate reductase; transfer may be stimulated by NADH. Binds one molecule of heme per monomer, possibly covalently. Heme binding is not affected by either [4Fe-4S] or S-adenosyl-L-methionine (SAM)-binding. Does not have coproporphyrinogen III dehydrogenase activity in vitro (PubMed:29282292). Binds 1 [4Fe-4S] cluster. The cluster is coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine (Probable). {ECO:0000269|PubMed:29282292, ECO:0000305|PubMed:29282292}.

## Biological Role

Component of heme chaperone HemW (complex.ecocyc.CPLX0-8291).

## Annotation

FUNCTION: Probably acts as a heme chaperone, transferring heme to the NarI subunit of the respiratory enzyme nitrate reductase; transfer may be stimulated by NADH. Binds one molecule of heme per monomer, possibly covalently. Heme binding is not affected by either [4Fe-4S] or S-adenosyl-L-methionine (SAM)-binding. Does not have coproporphyrinogen III dehydrogenase activity in vitro (PubMed:29282292). Binds 1 [4Fe-4S] cluster. The cluster is coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine (Probable). {ECO:0000269|PubMed:29282292, ECO:0000305|PubMed:29282292}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8291|complex.ecocyc.CPLX0-8291]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2955|gene.b2955]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52062`
- `KEGG:ecj:JW2922;eco:b2955;ecoc:C3026_16170;`
- `GeneID:947446;`
- `GO:GO:0004109; GO:0005737; GO:0006779; GO:0020037; GO:0042803; GO:0046872; GO:0051539`

## Notes

Heme chaperone HemW
