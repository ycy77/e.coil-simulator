---
entity_id: "protein.P11880"
entity_type: "protein"
name: "murF"
source_database: "UniProt"
source_id: "P11880"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02019, ECO:0000269|PubMed:2186811}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "murF mra b0086 JW0084"
---

# murF

`protein.P11880`

## Static

- Type: `protein`
- Source: `UniProt:P11880`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02019, ECO:0000269|PubMed:2186811}.

## Enriched Summary

FUNCTION: Involved in cell wall formation. Catalyzes the final step in the synthesis of UDP-N-acetylmuramoyl-pentapeptide, the precursor of murein. {ECO:0000255|HAMAP-Rule:MF_02019, ECO:0000269|PubMed:2186811}. UDP-N-acetylmuramoylalanyl-D-glutamyl-2,6-diaminopimelate-D-alanyl-D-alanine ligase (MurF) catalyzes the final cytoplasmic step in the biosynthesis of the peptidoglycan precursor . Data from kinetic characterization of the enzyme is consistent with a sequential ordered reaction mechanism, with sequential binding of ATP, tripeptide, and D-Ala-D-Ala . Carbamylation of the Lys202 residue is important for catalytic activity . A crystal structure of the apo-enzyme has been solved at 2.3Å resolution . A temperature-sensitive murF mutant has been isolated . The murF2 allele was determined to carry an A288T mutation in a conserved region of the enzyme; the mutant is 181-fold less catalytically active at the permissive temperature, with even lower activity at the nonpermissive temperature. Additional site-directed mutants in the conserved E158 and H188 residues have strongly reduced catalytic activity . MurF is a potential antimicrobial drug target; inhibitors of MurF activity have been identified . Reviews:

## Biological Role

Catalyzes UDP-N-acetylmuramoyl-L-alanyl-D-glutamyl-meso-2,6-diaminopimelate ligase (reaction.ecocyc.UDP-NACMURALGLDAPAALIG-RXN).

## Enriched Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Annotation

FUNCTION: Involved in cell wall formation. Catalyzes the final step in the synthesis of UDP-N-acetylmuramoyl-pentapeptide, the precursor of murein. {ECO:0000255|HAMAP-Rule:MF_02019, ECO:0000269|PubMed:2186811}.

## Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.UDP-NACMURALGLDAPAALIG-RXN|reaction.ecocyc.UDP-NACMURALGLDAPAALIG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0086|gene.b0086]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11880`
- `KEGG:ecj:JW0084;eco:b0086;ecoc:C3026_00335;`
- `GeneID:944813;`
- `GO:GO:0005524; GO:0005829; GO:0008360; GO:0008766; GO:0009252; GO:0047480; GO:0051301; GO:0071555`
- `EC:6.3.2.10`

## Notes

UDP-N-acetylmuramoyl-tripeptide--D-alanyl-D-alanine ligase (EC 6.3.2.10) (D-alanyl-D-alanine-adding enzyme) (UDP-MurNAc-pentapeptide synthetase)
