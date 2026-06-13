---
entity_id: "protein.P0AAX8"
entity_type: "protein"
name: "ybiS"
source_database: "UniProt"
source_id: "P0AAX8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybiS b0819 JW0803"
---

# ybiS

`protein.P0AAX8`

## Static

- Type: `protein`
- Source: `UniProt:P0AAX8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Responsible, at least in part, for anchoring of the major outer membrane lipoprotein (Lpp, also known as the Braun lipoprotein) to the peptidoglycan via a meso-diaminopimelyl-L-Lys- bond on the terminal residue of Lpp. Can be oxidized in vivo, its reduction depends preferentially on DsbG, although DsbC is able to partially replace DsbG. {ECO:0000269|PubMed:18456808}. LdtB is a periplasmic L,D-transpeptidase which cleaves the meso-diaminopimeloyl3→ D-alanine4 peptide bond in a peptidoglycan tetrapeptide stem and links the carboxyl group at the L-center of m-DAP3 to the side chain amine of the lysine residue located at the C terminus of CPLX0-8279 "Braun lipoprotein" . This activity anchors Braun lipoprotein to the peptidoglycan and contributes to the stability of the cell envelope. Muropeptides obtained from the peptidoglycan of an E. coli BW25113 Δ(G7073 "ldtA" ldtB G6571 "ldtC" G6904 "ldtE") quadruple mutant (BW25113Δ4) do not contain tripeptide stems substituted by a fragment of the Braun lipoprotein (see also ). Expression of ldtB in BW25113Δ4 restores the appearance of this muropeptide suggesting that LdtB catalyzes the covalent anchoring of Braun lipoprotein to the peptidoglycan . Complementation analysis suggests that E...

## Biological Role

Catalyzes RXN0-5401 (reaction.ecocyc.RXN0-5401).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Responsible, at least in part, for anchoring of the major outer membrane lipoprotein (Lpp, also known as the Braun lipoprotein) to the peptidoglycan via a meso-diaminopimelyl-L-Lys- bond on the terminal residue of Lpp. Can be oxidized in vivo, its reduction depends preferentially on DsbG, although DsbC is able to partially replace DsbG. {ECO:0000269|PubMed:18456808}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5401|reaction.ecocyc.RXN0-5401]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0819|gene.b0819]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAX8`
- `KEGG:ecj:JW0803;eco:b0819;ecoc:C3026_05150;`
- `GeneID:93776608;945441;`
- `GO:GO:0008360; GO:0016757; GO:0018104; GO:0030288; GO:0071555; GO:0071972`
- `EC:2.-.-.-`

## Notes

Probable L,D-transpeptidase YbiS (EC 2.-.-.-)
