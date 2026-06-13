---
entity_id: "protein.P22525"
entity_type: "protein"
name: "ycbB"
source_database: "UniProt"
source_id: "P22525"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycbB b0925 JW0908"
---

# ycbB

`protein.P22525`

## Static

- Type: `protein`
- Source: `UniProt:P22525`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Responsible, at least in part, for generating a meso-diaminopimelyl-3-a meso-diaminopimelyl-3 cross-link. {ECO:0000269|PubMed:18456808}. LdtD is a periplasmic L,D-transpeptidase that catalyses the formation of meso-diaminopimelyl → meso-diaminopimelyl cross links (also called DAP3→DAP3 or 3-3 cross-links) in peptidoglycan. LdtD cleaves the m-DAP3→D-ala4 peptide bond of an acyl donor stem tetrapeptide and links the carboxyl group at the L-center of m-DAP3 to the side chain amine of m-DAP3 of an acceptor stem peptide; LdtD can also use glycine as an acyl acceptor resulting in the formation of tetrapeptide stems ending in Gly and it can hydrolyse D-Ala4 in stem tetrapeptides with resultant formation of tripeptide stems. LdtD is a stress reponse L,D-transpeptidase with a role in the protective remodeling of peptidoglycan during cell envelope stress . Muropeptides obtained from the peptidoglycan of an G7073 ldtA G6422 ldtB G6571 ldtC ldtD G6904 ldtE quintuple mutant (BW25113Δ5) do not contain meso-DAP3-meso-DAP3 cross-links, tripeptide stems substituted by a fragment of the Braun lipoprotein, free tripeptide stems nor tetrapeptide stems with Gly as the fourth amino acid (see also ). Expression of ldtD in the BW25113Δ5 mutant restores production of meso-DAP3-meso-DAP3 cross-links, hydrolysis of D-Ala4, and exchange of D-Ala4 by Gly . E...

## Biological Role

Catalyzes RXN-16664 (reaction.ecocyc.RXN-16664), RXN-16665 (reaction.ecocyc.RXN-16665), RXN0-7489 (reaction.ecocyc.RXN0-7489).

## Annotation

FUNCTION: Responsible, at least in part, for generating a meso-diaminopimelyl-3-a meso-diaminopimelyl-3 cross-link. {ECO:0000269|PubMed:18456808}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-16664|reaction.ecocyc.RXN-16664]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-16665|reaction.ecocyc.RXN-16665]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7489|reaction.ecocyc.RXN0-7489]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0925|gene.b0925]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P22525`
- `KEGG:ecj:JW0908;eco:b0925;ecoc:C3026_05685;`
- `GeneID:945541;`
- `GO:GO:0004180; GO:0006974; GO:0008360; GO:0009252; GO:0016020; GO:0016757; GO:0016807; GO:0036460; GO:0046677; GO:0071555; GO:0071972`
- `EC:2.-.-.-`

## Notes

Probable L,D-transpeptidase YcbB (EC 2.-.-.-)
