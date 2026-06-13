---
entity_id: "protein.P76193"
entity_type: "protein"
name: "ynhG"
source_database: "UniProt"
source_id: "P76193"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ynhG b1678 JW1668"
---

# ynhG

`protein.P76193`

## Static

- Type: `protein`
- Source: `UniProt:P76193`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Responsible, at least in part, for generating a meso-diaminopimelyl-3-a meso-diaminopimelyl-3 cross-link. {ECO:0000269|PubMed:18456808}. LdtE (formerly YnhG) is a membrane anchored, periplasmic L,D-transpeptidase that catalyses the formation of meso-diaminopimelate→meso-diaminopimelate cross links (also called DAP3→DAP3 or 3-3 cross-links) in peptidoglycan; LdtE cleaves the m-DAP3→D-ala4 peptide bond of an acyl donor stem tetrapeptide and links the carboxyl group at the L-center of m-DAP3 to the side chain amine of m-DAP3 of an acceptor stem peptide. Muropeptides obtained from the peptidoglycan of a BW25113Δ(G7073 "ldtA" G6422 "ldtB" G6571 "ldtC" ldtE) quadruple mutant (BW25113Δ4) do not contain tripeptide stems substituted by a fragment of the Braun lipoprotein ; muropeptides obtained from the peptidoglycan of a BW25113Δ(ldtA ldtB ldtC EG11253 "ldtD" ldtE) quintuple mutant (BW25113Δ5) do not contain tripeptide stems substituted by a fragment of the Braun lipoprotein, nor do they contain meso-DAP3-meso-DAP3 cross-links, free tripeptide stems or tetrapeptide stems with Gly as the fourth amino acid . Expression of ldtE in the BW25113Δ4 mutant increases the amount of muropeptides with DAP3-DAP3 cross links...

## Biological Role

Catalyzes RXN0-7489 (reaction.ecocyc.RXN0-7489).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Responsible, at least in part, for generating a meso-diaminopimelyl-3-a meso-diaminopimelyl-3 cross-link. {ECO:0000269|PubMed:18456808}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7489|reaction.ecocyc.RXN0-7489]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1678|gene.b1678]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76193`
- `KEGG:ecj:JW1668;eco:b1678;ecoc:C3026_09615;`
- `GeneID:946174;`
- `GO:GO:0008360; GO:0009252; GO:0016757; GO:0018104; GO:0042597; GO:0071555; GO:0071972`
- `EC:2.-.-.-`

## Notes

Probable L,D-transpeptidase YnhG (EC 2.-.-.-)
