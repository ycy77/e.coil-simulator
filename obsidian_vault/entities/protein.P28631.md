---
entity_id: "protein.P28631"
entity_type: "protein"
name: "holB"
source_database: "UniProt"
source_id: "P28631"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "holB b1099 JW1085"
---

# holB

`protein.P28631`

## Static

- Type: `protein`
- Source: `UniProt:P28631`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Part of the beta sliding clamp loading complex, which hydrolyzes ATP to load the beta clamp onto primed DNA to form the DNA replication pre-initiation complex (PubMed:2040637). DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. This DNA polymerase also exhibits 3' to 5' exonuclease activity. The gamma complex (gamma(3),delta,delta') is thought to load beta dimers onto DNA by binding ATP which alters the complex's conformation so it can bind beta sliding clamp dimers and open them at one interface. Primed DNA is recognized, ATP is hydrolyzed releasing the gamma complex and closing the beta sliding clamp ring around the primed DNA (PubMed:9927437). {ECO:0000269|PubMed:2040637, ECO:0000269|PubMed:9927437}. The crystal structure of delta' has been determined. It is composed of three domains arranged in a "C" shape, with a nonfunctional nucleotide binding site in its amino-terminus .

## Biological Role

Catalyzes deoxyadenosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00375), deoxyguanosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00376), deoxycytidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00377), deoxythymidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00378), deoxynucleoside triphosphate:DNA deoxynucleotidyltransferase (reaction.R00379). Component of replisome (complex.ecocyc.CPLX0-13320), DNA polymerase III, clamp-loader complex (complex.ecocyc.CPLX0-3801), DNA polymerase III, holoenzyme (complex.ecocyc.CPLX0-3803).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: Part of the beta sliding clamp loading complex, which hydrolyzes ATP to load the beta clamp onto primed DNA to form the DNA replication pre-initiation complex (PubMed:2040637). DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. This DNA polymerase also exhibits 3' to 5' exonuclease activity. The gamma complex (gamma(3),delta,delta') is thought to load beta dimers onto DNA by binding ATP which alters the complex's conformation so it can bind beta sliding clamp dimers and open them at one interface. Primed DNA is recognized, ATP is hydrolyzed releasing the gamma complex and closing the beta sliding clamp ring around the primed DNA (PubMed:9927437). {ECO:0000269|PubMed:2040637, ECO:0000269|PubMed:9927437}.

## Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Outgoing Edges (8)

- `catalyzes` --> [[reaction.R00375|reaction.R00375]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00376|reaction.R00376]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00377|reaction.R00377]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00378|reaction.R00378]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00379|reaction.R00379]] `KEGG` `database` - via EC:2.7.7.7
- `is_component_of` --> [[complex.ecocyc.CPLX0-13320|complex.ecocyc.CPLX0-13320]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-3801|complex.ecocyc.CPLX0-3801]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-3803|complex.ecocyc.CPLX0-3803]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1099|gene.b1099]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P28631`
- `KEGG:ecj:JW1085;eco:b1099;ecoc:C3026_06640;`
- `GeneID:75203685;945661;`
- `GO:GO:0003677; GO:0003689; GO:0003887; GO:0006260; GO:0006261; GO:0008408; GO:0009360; GO:0030894; GO:0043846`
- `EC:2.7.7.7`

## Notes

DNA polymerase III subunit delta' (EC 2.7.7.7)
