---
entity_id: "protein.P0ABS8"
entity_type: "protein"
name: "holE"
source_database: "UniProt"
source_id: "P0ABS8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "holE b1842 JW1831"
---

# holE

`protein.P0ABS8`

## Static

- Type: `protein`
- Source: `UniProt:P0ABS8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. This DNA polymerase also exhibits 3' to 5' exonuclease activity.; FUNCTION: The exact function of the theta subunit is unknown. The theta subunit of DNA polymerase III (HolE) binds tightly to the epsilon subunit but not to the alpha subunit . This binding appears to enhance interaction between alpha and epsilon as well as slightly stimulating epsilon proofreading activity . Loss of theta yields no significant growth phenotype, and theta does not appear to be required for speed or processivity of DNA polymerase III holoenzyme . Theta may enhance the stability of epsilon . HolE may have a "moonlighting" function in the cell. Both YdgT and HolE appear to influence expression of EG11005 tnaA by enhancing transcription termination at the leader DNA sequence . Based on an NMR characterization, the surface of theta is bipolar, with the positive and negative charges grouped at opposite ends of the protein . It also appears to have exposed hydrophobic residues . A solution structure of the theta in a complex with the N-terminal domain of epsilon has been solved . A holE deletion strain appears to contain a lower amount of unassociated epsilon subunit...

## Biological Role

Catalyzes deoxyadenosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00375), deoxyguanosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00376), deoxycytidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00377), deoxythymidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00378), deoxynucleoside triphosphate:DNA deoxynucleotidyltransferase (reaction.R00379). Component of replisome (complex.ecocyc.CPLX0-13320), DNA polymerase III, core enzyme (complex.ecocyc.CPLX0-2361), DNA polymerase III, holoenzyme (complex.ecocyc.CPLX0-3803).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. This DNA polymerase also exhibits 3' to 5' exonuclease activity.; FUNCTION: The exact function of the theta subunit is unknown.

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
- `is_component_of` --> [[complex.ecocyc.CPLX0-13320|complex.ecocyc.CPLX0-13320]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.CPLX0-2361|complex.ecocyc.CPLX0-2361]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-3803|complex.ecocyc.CPLX0-3803]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b1842|gene.b1842]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABS8`
- `KEGG:ecj:JW1831;eco:b1842;ecoc:C3026_10495;`
- `GeneID:93776109;947471;`
- `GO:GO:0003677; GO:0003887; GO:0005829; GO:0006261; GO:0006272; GO:0006273; GO:0009360; GO:0030894; GO:0044776`
- `EC:2.7.7.7`

## Notes

DNA polymerase III subunit theta (EC 2.7.7.7)
