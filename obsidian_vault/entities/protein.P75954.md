---
entity_id: "protein.P75954"
entity_type: "protein"
name: "ycfS"
source_database: "UniProt"
source_id: "P75954"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycfS b1113 JW5820"
---

# ycfS

`protein.P75954`

## Static

- Type: `protein`
- Source: `UniProt:P75954`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Responsible, at least in part, for anchoring of the major outer membrane lipoprotein (Lpp, also known as the Braun lipoprotein) to the peptidoglycan via a meso-diaminopimelyl-L-Lys- bond on the terminal residue of Lpp. {ECO:0000269|PubMed:18456808}. LdtC is an L,D-transpeptidase which cleaves the meso-diaminopimeloyl3→ D-alanine4 peptide bond in a peptidoglycan tetrapeptide stem and links the carboxyl group at the L-center of m-DAP3 to the side chain amine of the lysine residue located at the C terminus of CPLX0-8279 "Braun lipoprotein" . This activity anchors Braun lipoprotein to the peptidoglycan and contributes to the stability of the cell envelope. Muropeptides obtained from the peptidoglycan of an E. coli BW25113 Δ(G7073 "ldtA" G6422 "ldtB" ldtC G6904 "ldtE") quadruple mutant (BW25113Δ4) do not contain tripeptide stems substituted by a fragment of the Braun lipoprotein (see also ). Expression of ldtC in BW25113Δ4 restores the appearance of this muropeptide suggesting that LdtC catalyzes the covalent anchoring of Braun lipoprotein to the peptidoglycan . Complementation analysis suggests that E. coli K-12 contains three L,D transpeptidases (LdtA, LdtB and LdtC) that can catalyse the covalent anchoring of Braun lipoprotein to the peptidoglycan however the analysis of single deletion mutants suggests LdtB may be of primary importance ( ('results not shown'). An E...

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

- `encodes` <-- [[gene.b1113|gene.b1113]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75954`
- `KEGG:ecj:JW5820;eco:b1113;`
- `GeneID:945666;`
- `GO:GO:0008360; GO:0016757; GO:0018104; GO:0042597; GO:0071555; GO:0071972`
- `EC:2.-.-.-`

## Notes

Probable L,D-transpeptidase YcfS (EC 2.-.-.-)
