---
entity_id: "protein.P39176"
entity_type: "protein"
name: "erfK"
source_database: "UniProt"
source_id: "P39176"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "erfK yeeG yzzT b1990 JW1968"
---

# erfK

`protein.P39176`

## Static

- Type: `protein`
- Source: `UniProt:P39176`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Responsible, at least in part, for anchoring of the major outer membrane lipoprotein (Lpp, also known as the Braun lipoprotein) to the peptidoglycan via a meso-diaminopimelyl-L-Lys- bond on the terminal residue of Lpp. {ECO:0000269|PubMed:18456808}. LdtA is an L,D-transpeptidase which cleaves the meso-diaminopimeloyl3→ D-alanine4 peptide bond in a peptidoglycan tetrapeptide stem and links the carboxyl group at the L-center of m-DAP3 to the side chain amine of the lysine residue located at the C terminus of CPLX0-8279 "Braun lipoprotein" . This activity anchors Braun lipoprotein to the peptidoglycan and contributes to the stability of the cell envelope. Muropeptides obtained from the peptidoglycan of an E. coli BW25113 Δ(ldtA G6422 "ldtB" G6571 "ldtC" G6904 "ldtE") quadruple mutant (BW25113Δ4) do not contain tripeptide stems substituted by a fragment of the Braun lipoprotein (see also ). Expression of ldtA in BW25113Δ4 restores the appearance of this muropeptide suggesting that LdtA catalyzes the covalent anchoring of Braun lipoprotein to the peptidoglycan . Complementation analysis suggests that E. coli K-12 contains three L,D transpeptidases (LdtA, LdtB and LdtC) that can catalyse the covalent anchoring of Braun lipoprotein to the peptidoglycan however the analysis of single deletion mutants suggests LdtB may be of primary importance ( 'results not shown'). An E...

## Biological Role

Catalyzes RXN0-5401 (reaction.ecocyc.RXN0-5401).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Responsible, at least in part, for anchoring of the major outer membrane lipoprotein (Lpp, also known as the Braun lipoprotein) to the peptidoglycan via a meso-diaminopimelyl-L-Lys- bond on the terminal residue of Lpp. {ECO:0000269|PubMed:18456808}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5401|reaction.ecocyc.RXN0-5401]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1990|gene.b1990]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39176`
- `KEGG:ecj:JW1968;eco:b1990;ecoc:C3026_11230;`
- `GeneID:945273;`
- `GO:GO:0008360; GO:0016757; GO:0018104; GO:0042597; GO:0071555; GO:0071972`
- `EC:2.-.-.-`

## Notes

Probable L,D-transpeptidase ErfK/SrfK (EC 2.-.-.-)
