---
entity_id: "protein.P28630"
entity_type: "protein"
name: "holA"
source_database: "UniProt"
source_id: "P28630"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "holA b0640 JW0635"
---

# holA

`protein.P28630`

## Static

- Type: `protein`
- Source: `UniProt:P28630`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Part of the beta sliding clamp loading complex, which hydrolyzes ATP to load the beta clamp onto primed DNA to form the DNA replication pre-initiation complex (PubMed:2040637). DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. This DNA polymerase also exhibits 3'-5' exonuclease activity. The delta subunit is the wrench that will open the beta subunit dimer, which has been modeled to leave a gap large enough for ssDNA to pass through (PubMed:11525728). The gamma complex (gamma(3),delta,delta') is thought to load beta dimers onto DNA by binding ATP which alters the complex's conformation so it can bind beta sliding clamp dimers and open them at one interface. Primed DNA is recognized, ATP is hydrolyzed releasing the gamma complex and closing the beta sliding clamp ring around the primed DNA (PubMed:9927437). {ECO:0000269|PubMed:2040637, ECO:0000269|PubMed:9927437, ECO:0000305|PubMed:11525728}. Some delta subunits exist independent of the CPLX0-3801, possibly playing a role in stripping the CPLX0-3761 from DNA in the absence of the clamp-loader complex . The clamp-loader complex binds primed ssDNA and loads the β sliding clamp. Following this, the CPLX0-2361, linked by the EG10245-MONOMER tau subunit, binds, allowing processive DNA polymerization .

## Biological Role

Catalyzes deoxyadenosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00375), deoxyguanosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00376), deoxycytidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00377), deoxythymidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00378), deoxynucleoside triphosphate:DNA deoxynucleotidyltransferase (reaction.R00379). Component of replisome (complex.ecocyc.CPLX0-13320), DNA polymerase III, clamp-loader complex (complex.ecocyc.CPLX0-3801), DNA polymerase III, holoenzyme (complex.ecocyc.CPLX0-3803).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: Part of the beta sliding clamp loading complex, which hydrolyzes ATP to load the beta clamp onto primed DNA to form the DNA replication pre-initiation complex (PubMed:2040637). DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. This DNA polymerase also exhibits 3'-5' exonuclease activity. The delta subunit is the wrench that will open the beta subunit dimer, which has been modeled to leave a gap large enough for ssDNA to pass through (PubMed:11525728). The gamma complex (gamma(3),delta,delta') is thought to load beta dimers onto DNA by binding ATP which alters the complex's conformation so it can bind beta sliding clamp dimers and open them at one interface. Primed DNA is recognized, ATP is hydrolyzed releasing the gamma complex and closing the beta sliding clamp ring around the primed DNA (PubMed:9927437). {ECO:0000269|PubMed:2040637, ECO:0000269|PubMed:9927437, ECO:0000305|PubMed:11525728}.

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

- `encodes` <-- [[gene.b0640|gene.b0640]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P28630`
- `KEGG:ecj:JW0635;eco:b0640;ecoc:C3026_03200;`
- `GeneID:75204999;947573;`
- `GO:GO:0003677; GO:0003689; GO:0003887; GO:0006260; GO:0006261; GO:0009360; GO:0030894; GO:0043846`
- `EC:2.7.7.7`

## Notes

DNA polymerase III subunit delta (EC 2.7.7.7)
