---
entity_id: "protein.P06710"
entity_type: "protein"
name: "dnaX"
source_database: "UniProt"
source_id: "P06710"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dnaX dnaZ dnaZX b0470 JW0459"
---

# dnaX

`protein.P06710`

## Static

- Type: `protein`
- Source: `UniProt:P06710`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Part of the beta sliding clamp loading complex, which hydrolyzes ATP to load the beta clamp onto primed DNA to form the DNA replication pre-initiation complex (PubMed:2040637). DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. This DNA polymerase also exhibits 3'-5' exonuclease activity. The gamma complex (gamma(3),delta,delta') is thought to load beta dimers onto DNA by binding ATP which alters the complex's conformation so it can bind beta sliding clamp dimers and open them at one interface. Primed DNA is recognized, ATP is hydrolyzed releasing the gamma complex and closing the beta sliding clamp ring around the primed DNA (PubMed:9927437). {ECO:0000269|PubMed:2040637}.; FUNCTION: [Isoform tau]: Serves as a scaffold to trimerize the core complex (PubMed:7037770). {ECO:0000305|PubMed:7037770}.; FUNCTION: [Isoform gamma]: Interacts with the delta and delta' subunits to transfer the beta subunit on the DNA (PubMed:9927437). Interacts with ATP, drives ATP-induced conformational changes in the gamma complex that opens the beta sliding clamp ring. After loading of primed DNA ATP is hydrolyzed and the beta sliding clamp ring closes (PubMed:9927437). {ECO:0000269|PubMed:9927437}...

## Biological Role

Catalyzes deoxyadenosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00375), deoxyguanosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00376), deoxycytidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00377), deoxythymidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00378), deoxynucleoside triphosphate:DNA deoxynucleotidyltransferase (reaction.R00379). Component of replisome (complex.ecocyc.CPLX0-13320), DNA polymerase III, clamp-loader complex (complex.ecocyc.CPLX0-3801), DNA polymerase III τ dimer (complex.ecocyc.CPLX0-3802), DNA polymerase III, holoenzyme (complex.ecocyc.CPLX0-3803).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: Part of the beta sliding clamp loading complex, which hydrolyzes ATP to load the beta clamp onto primed DNA to form the DNA replication pre-initiation complex (PubMed:2040637). DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. This DNA polymerase also exhibits 3'-5' exonuclease activity. The gamma complex (gamma(3),delta,delta') is thought to load beta dimers onto DNA by binding ATP which alters the complex's conformation so it can bind beta sliding clamp dimers and open them at one interface. Primed DNA is recognized, ATP is hydrolyzed releasing the gamma complex and closing the beta sliding clamp ring around the primed DNA (PubMed:9927437). {ECO:0000269|PubMed:2040637}.; FUNCTION: [Isoform tau]: Serves as a scaffold to trimerize the core complex (PubMed:7037770). {ECO:0000305|PubMed:7037770}.; FUNCTION: [Isoform gamma]: Interacts with the delta and delta' subunits to transfer the beta subunit on the DNA (PubMed:9927437). Interacts with ATP, drives ATP-induced conformational changes in the gamma complex that opens the beta sliding clamp ring. After loading of primed DNA ATP is hydrolyzed and the beta sliding clamp ring closes (PubMed:9927437). {ECO:0000269|PubMed:9927437}.

## Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Outgoing Edges (9)

- `catalyzes` --> [[reaction.R00375|reaction.R00375]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00376|reaction.R00376]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00377|reaction.R00377]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00378|reaction.R00378]] `KEGG` `database` - via EC:2.7.7.7
- `catalyzes` --> [[reaction.R00379|reaction.R00379]] `KEGG` `database` - via EC:2.7.7.7
- `is_component_of` --> [[complex.ecocyc.CPLX0-13320|complex.ecocyc.CPLX0-13320]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2 | EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.CPLX0-3801|complex.ecocyc.CPLX0-3801]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.CPLX0-3802|complex.ecocyc.CPLX0-3802]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-3803|complex.ecocyc.CPLX0-3803]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0470|gene.b0470]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06710`
- `KEGG:ecj:JW0459;eco:b0470;ecoc:C3026_02310;`
- `GeneID:945105;`
- `GO:GO:0003677; GO:0003689; GO:0003887; GO:0005524; GO:0006260; GO:0006261; GO:0009360; GO:0016887; GO:0017111; GO:0030337; GO:0030894; GO:0042802; GO:0043846; GO:0046872; GO:0075523`
- `EC:2.7.7.7`

## Notes

DNA polymerase III subunit tau (EC 2.7.7.7) (DNA polymerase III subunit gamma)
