---
entity_id: "protein.P11454"
entity_type: "protein"
name: "entF"
source_database: "UniProt"
source_id: "P11454"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:10692387}. Note=Membrane-associated. {ECO:0000269|PubMed:10692387}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "entF b0586 JW0578"
---

# entF

`protein.P11454`

## Static

- Type: `protein`
- Source: `UniProt:P11454`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:10692387}. Note=Membrane-associated. {ECO:0000269|PubMed:10692387}.

## Enriched Summary

FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (enterochelin), which is a macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine (PubMed:1338974, PubMed:1826089, PubMed:216414, PubMed:9485415). EntF catalyzes the activation of L-serine via ATP-dependent PPi exchange reaction to form seryladenylate (PubMed:10688898, PubMed:1338974, PubMed:1826089, PubMed:9485415). Activated L-serine is loaded onto the peptidyl carrier domain via a thioester linkage to the phosphopanthetheine moiety, forming seryl-S-Ppant-EntF (PubMed:9485415). EntF acts then as the sole catalyst for the formation of the three amide and three ester linkages found in enterobactin, using seryladenylate and 2,3-dihydroxybenzoate-S-Ppant-EntB (DHB-S-Ppant-EntB) as substrates, via the formation of a DHB-Ser-S-Ppant-EntF intermediate (PubMed:9485415). {ECO:0000269|PubMed:10688898, ECO:0000269|PubMed:1338974, ECO:0000269|PubMed:1826089, ECO:0000269|PubMed:216414, ECO:0000269|PubMed:9485415}. ENTF-MONOMER, the entF gene product, activates L-serine through an ATP-pyrophosphate exchange reaction at the carboxylate group of L-serine. The resulting aminoacyladenylate remains enzyme-bound for further reactions in the ENTBACSYN-PWY pathway. The enzyme also contains a covalently bound phosphopantetheine moiety that is the result of an EntD catalyzed activation reaction...

## Biological Role

Catalyzes ENTG-RXN (reaction.ecocyc.ENTG-RXN), RXN-15891 (reaction.ecocyc.RXN-15891), RXN-19474 (reaction.ecocyc.RXN-19474). Component of enterobactin synthase (complex.ecocyc.ENTMULTI-CPLX). Bound by Magnesium cation (molecule.C00305), Pantetheine 4'-phosphate (molecule.C01134).

## Enriched Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (enterochelin), which is a macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine (PubMed:1338974, PubMed:1826089, PubMed:216414, PubMed:9485415). EntF catalyzes the activation of L-serine via ATP-dependent PPi exchange reaction to form seryladenylate (PubMed:10688898, PubMed:1338974, PubMed:1826089, PubMed:9485415). Activated L-serine is loaded onto the peptidyl carrier domain via a thioester linkage to the phosphopanthetheine moiety, forming seryl-S-Ppant-EntF (PubMed:9485415). EntF acts then as the sole catalyst for the formation of the three amide and three ester linkages found in enterobactin, using seryladenylate and 2,3-dihydroxybenzoate-S-Ppant-EntB (DHB-S-Ppant-EntB) as substrates, via the formation of a DHB-Ser-S-Ppant-EntF intermediate (PubMed:9485415). {ECO:0000269|PubMed:10688898, ECO:0000269|PubMed:1338974, ECO:0000269|PubMed:1826089, ECO:0000269|PubMed:216414, ECO:0000269|PubMed:9485415}.

## Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.ENTG-RXN|reaction.ecocyc.ENTG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-15891|reaction.ecocyc.RXN-15891]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19474|reaction.ecocyc.RXN-19474]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.ENTMULTI-CPLX|complex.ecocyc.ENTMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C01134|molecule.C01134]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0586|gene.b0586]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11454`
- `KEGG:ecj:JW0578;eco:b0586;ecoc:C3026_02925;`
- `GeneID:945184;`
- `GO:GO:0005524; GO:0005737; GO:0005829; GO:0005886; GO:0009239; GO:0009366; GO:0016779; GO:0031177; GO:0043041; GO:0047527`
- `EC:6.2.1.72; 6.3.2.14`

## Notes

Enterobactin synthase component F (EC 6.3.2.14) (Enterochelin synthase F) (Nonribosomal peptide synthetase EntF) [Includes: L-serine--[L-seryl-carrier protein] ligase (EC 6.2.1.72) (Serine-activating enzyme) (Seryl-AMP ligase)]
