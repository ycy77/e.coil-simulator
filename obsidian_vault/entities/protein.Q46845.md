---
entity_id: "protein.Q46845"
entity_type: "protein"
name: "yghU"
source_database: "UniProt"
source_id: "Q46845"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yghU b2989 JW5492"
---

# yghU

`protein.Q46845`

## Static

- Type: `protein`
- Source: `UniProt:Q46845`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Exhibits a robust glutathione (GSH)-dependent disulfide-bond reductase activity toward the model substrate, 2-hydroxyethyl disulfide; the actual physiological substrates are not known. Also displays a modest GSH-dependent peroxidase activity toward several organic hydroperoxides, such as cumene hydroperoxide and linoleic acid 13(S)-hydroperoxide, but does not reduce H(2)O(2) or tert-butyl hydroperoxide at appreciable rates. Exhibits little or no GSH transferase activity with most typical electrophilic substrates, and has no detectable transferase activity toward 1-chloro-2,4-dinitrobenzene (CDNB) with glutathionylspermidine (GspSH) as the nucleophilic substrate. {ECO:0000269|PubMed:21222452}.

## Biological Role

Component of disulfide reductase / organic hydroperoxide reductase (complex.ecocyc.CPLX0-7917).

## Annotation

FUNCTION: Exhibits a robust glutathione (GSH)-dependent disulfide-bond reductase activity toward the model substrate, 2-hydroxyethyl disulfide; the actual physiological substrates are not known. Also displays a modest GSH-dependent peroxidase activity toward several organic hydroperoxides, such as cumene hydroperoxide and linoleic acid 13(S)-hydroperoxide, but does not reduce H(2)O(2) or tert-butyl hydroperoxide at appreciable rates. Exhibits little or no GSH transferase activity with most typical electrophilic substrates, and has no detectable transferase activity toward 1-chloro-2,4-dinitrobenzene (CDNB) with glutathionylspermidine (GspSH) as the nucleophilic substrate. {ECO:0000269|PubMed:21222452}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7917|complex.ecocyc.CPLX0-7917]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2989|gene.b2989]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46845`
- `KEGG:ecj:JW5492;eco:b2989;ecoc:C3026_16350;`
- `GeneID:75173122;947472;`
- `GO:GO:0004364; GO:0004601; GO:0005737; GO:0015036; GO:0042803`
- `EC:1.11.1.-; 1.8.4.-`

## Notes

Disulfide-bond oxidoreductase YghU (EC 1.8.4.-) (GSH-dependent disulfide-bond oxidoreductase YghU) (GST N2-2) (Organic hydroperoxidase) (EC 1.11.1.-)
