---
entity_id: "protein.P04805"
entity_type: "protein"
name: "gltX"
source_database: "UniProt"
source_id: "P04805"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00022}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gltX b2400 JW2395"
---

# gltX

`protein.P04805`

## Static

- Type: `protein`
- Source: `UniProt:P04805`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00022}.

## Enriched Summary

FUNCTION: Catalyzes the attachment of glutamate to tRNA(Glu) in a two-step reaction: glutamate is first activated by ATP to form Glu-AMP and then transferred to the acceptor end of tRNA(Glu). {ECO:0000269|PubMed:14764088, ECO:0000269|PubMed:6280993, ECO:0000269|PubMed:6986385, ECO:0000269|PubMed:7797500, ECO:0000269|PubMed:8218204}.; FUNCTION: Phosphorylation of GltX by HipA prevents it from being charged, leading to an increase in uncharged tRNA(Glu). This induces amino acid starvation and the stringent response via RelA/SpoT and increased (p)ppGpp levels, which inhibits replication, transcription, translation and cell wall synthesis, reducing growth and leading to multidrug resistance and persistence (PubMed:24095282, PubMed:24343429). Overexpression of GltX prevents HipA-induced growth arrest, persister formation and increases in (p)ppGpp levels (PubMed:24343429, PubMed:28430938). {ECO:0000269|PubMed:24095282, ECO:0000269|PubMed:24343429, ECO:0000269|PubMed:28430938}. Glutamate-tRNA ligase (GluRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. GluRS belongs to the Class IB aminoacyl-tRNA synthetases . GluRS charges tRNAGlu for both protein and δ-aminolevulinic acid (ALA) synthesis...

## Biological Role

Catalyzes GLURS-RXN (reaction.ecocyc.GLURS-RXN). Bound by Zinc cation (molecule.C00038), Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the attachment of glutamate to tRNA(Glu) in a two-step reaction: glutamate is first activated by ATP to form Glu-AMP and then transferred to the acceptor end of tRNA(Glu). {ECO:0000269|PubMed:14764088, ECO:0000269|PubMed:6280993, ECO:0000269|PubMed:6986385, ECO:0000269|PubMed:7797500, ECO:0000269|PubMed:8218204}.; FUNCTION: Phosphorylation of GltX by HipA prevents it from being charged, leading to an increase in uncharged tRNA(Glu). This induces amino acid starvation and the stringent response via RelA/SpoT and increased (p)ppGpp levels, which inhibits replication, transcription, translation and cell wall synthesis, reducing growth and leading to multidrug resistance and persistence (PubMed:24095282, PubMed:24343429). Overexpression of GltX prevents HipA-induced growth arrest, persister formation and increases in (p)ppGpp levels (PubMed:24343429, PubMed:28430938). {ECO:0000269|PubMed:24095282, ECO:0000269|PubMed:24343429, ECO:0000269|PubMed:28430938}.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLURS-RXN|reaction.ecocyc.GLURS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2400|gene.b2400]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04805`
- `KEGG:ecj:JW2395;eco:b2400;ecoc:C3026_13335;`
- `GeneID:93774730;946906;`
- `GO:GO:0000049; GO:0004818; GO:0005524; GO:0005829; GO:0006424; GO:0008270`
- `EC:6.1.1.17`

## Notes

Glutamate--tRNA ligase (EC 6.1.1.17) (Glutamyl-tRNA synthetase) (GluRS)
