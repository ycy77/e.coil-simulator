---
entity_id: "protein.P0A927"
entity_type: "protein"
name: "tsx"
source_database: "UniProt"
source_id: "P0A927"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:3276691, ECO:0000269|PubMed:791677}; Multi-pass membrane protein {ECO:0000305|PubMed:2458926, ECO:0000305|PubMed:3276691}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tsx nupA b0411 JW0401"
---

# tsx

`protein.P0A927`

## Static

- Type: `protein`
- Source: `UniProt:P0A927`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:3276691, ECO:0000269|PubMed:791677}; Multi-pass membrane protein {ECO:0000305|PubMed:2458926, ECO:0000305|PubMed:3276691}.

## Enriched Summary

FUNCTION: Functions as a substrate-specific channel for nucleosides and deoxynucleosides (PubMed:2458926, PubMed:3276691, PubMed:791677). Has a greater affinity for deoxynucleosides than for nucleosides, and does not transport free bases (PubMed:2458926). In addition, constitutes the receptor for colicin K and phage T6 (PubMed:3276691, PubMed:791677). {ECO:0000269|PubMed:2458926, ECO:0000269|PubMed:3276691, ECO:0000269|PubMed:791677}.; FUNCTION: (Microbial infection) Serves as a receptor for CdiA-STECO31, required for adhesion between E.coli expressing CdiA-STECO31 and this strain. {ECO:0000269|PubMed:28351921}. Tsx is an outer membrane porin which is responsible for the uptake of nucleosides and deoxynucleosides at sub-uM concentrations . Reconstitution of purified Tsx into lipid bilayer membranes suggests that Tsx has a greater affinity for deoxynucleosides than for nucleosides and that it does not play a role in the transport of nucleobases . Tsx forms a monomeric β-barrel consisting of 12 β strands . In addition to being a channel for (deoxy)nucleosides Tsx functions as a receptor for bacteriophage and colicins and transports the antibiotic, albicidin . Tsx is the primary receptor for the uncharacterized environmental phage isolate U115 (see further ). Tsx is down-regulated when E...

## Biological Role

Catalyzes TRANS-RXN0-468 (reaction.ecocyc.TRANS-RXN0-468).

## Annotation

FUNCTION: Functions as a substrate-specific channel for nucleosides and deoxynucleosides (PubMed:2458926, PubMed:3276691, PubMed:791677). Has a greater affinity for deoxynucleosides than for nucleosides, and does not transport free bases (PubMed:2458926). In addition, constitutes the receptor for colicin K and phage T6 (PubMed:3276691, PubMed:791677). {ECO:0000269|PubMed:2458926, ECO:0000269|PubMed:3276691, ECO:0000269|PubMed:791677}.; FUNCTION: (Microbial infection) Serves as a receptor for CdiA-STECO31, required for adhesion between E.coli expressing CdiA-STECO31 and this strain. {ECO:0000269|PubMed:28351921}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-468|reaction.ecocyc.TRANS-RXN0-468]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0411|gene.b0411]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A927`
- `KEGG:ecj:JW0401;eco:b0411;ecoc:C3026_02005;`
- `GeneID:75170428;75202833;946242;`
- `GO:GO:0006811; GO:0009279; GO:0015471; GO:0015858; GO:0046718; GO:0046930`

## Notes

Nucleoside-specific channel-forming protein Tsx
