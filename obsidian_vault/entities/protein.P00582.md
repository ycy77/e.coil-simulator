---
entity_id: "protein.P00582"
entity_type: "protein"
name: "polA"
source_database: "UniProt"
source_id: "P00582"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "polA resA b3863 JW3835"
---

# polA

`protein.P00582`

## Static

- Type: `protein`
- Source: `UniProt:P00582`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: In addition to polymerase activity, this DNA polymerase exhibits 3'-5' and 5'-3' exonuclease activity. It is able to utilize nicked circular duplex DNA as a template and can unwind the parental DNA strand from its template.; FUNCTION: Genetic interactions among priB, dam, lexA, nagC, polA, rdgB, rdgB, rep and uup link the PriA-PriB replication restart pathway to DNA double-strand break repair. {ECO:0000269|PubMed:36326440}. DNA Polymerase I (Pol I) is a multifunctional enzyme that combines a DNA polymerase activity, "flap-directed" 5' nuclease activity, and a 3' to 5' proofreading exonuclease activity. It is required for several types of DNA repair and is the primary enzyme responsible for Okazaki fragment maturation, i.e. removing RNA primers from newly-synthesized DNA and replacing them with DNA. Pol I is involved in several DNA repair pathways. It is required for excision repair, displacing the UvrABC nuclease and patching the gap it leaves behind . Pol I is also required in MutHLS-mediated very short patch repair . Pol I can excise and replace pyrimidine dimers directly . It also cleaves the faulty nucleotide from abasic lesion sites following nicking by endonuclease III . Finally, Pol I is generally involved in postreplication repair of DNA gaps and double-strand breaks...

## Biological Role

Catalyzes deoxyadenosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00375), deoxyguanosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00376), deoxycytidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00377), deoxythymidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00378), deoxynucleoside triphosphate:DNA deoxynucleotidyltransferase (reaction.R00379), DNA-DIRECTED-DNA-POLYMERASE-RXN (reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN), RXN0-4961 (reaction.ecocyc.RXN0-4961), RXN0-5039 (reaction.ecocyc.RXN0-5039). Bound by Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03410` Base excision repair (KEGG)
- `eco03420` Nucleotide excision repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: In addition to polymerase activity, this DNA polymerase exhibits 3'-5' and 5'-3' exonuclease activity. It is able to utilize nicked circular duplex DNA as a template and can unwind the parental DNA strand from its template.; FUNCTION: Genetic interactions among priB, dam, lexA, nagC, polA, rdgB, rdgB, rep and uup link the PriA-PriB replication restart pathway to DNA double-strand break repair. {ECO:0000269|PubMed:36326440}.

## Pathways

- `eco03030` DNA replication (KEGG)
- `eco03410` Base excision repair (KEGG)
- `eco03420` Nucleotide excision repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Outgoing Edges (8)

- `catalyzes` --> [[reaction.R00375|reaction.R00375]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00376|reaction.R00376]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00377|reaction.R00377]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00378|reaction.R00378]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00379|reaction.R00379]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN|reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-4961|reaction.ecocyc.RXN0-4961]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5039|reaction.ecocyc.RXN0-5039]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3863|gene.b3863]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00582`
- `KEGG:ecj:JW3835;eco:b3863;ecoc:C3026_20885;`
- `GeneID:93778073;948356;`
- `GO:GO:0003677; GO:0003887; GO:0005737; GO:0005829; GO:0006260; GO:0006261; GO:0006281; GO:0006284; GO:0006302; GO:0008408; GO:0008409`
- `EC:2.7.7.7`

## Notes

DNA polymerase I (POL I) (EC 2.7.7.7)
