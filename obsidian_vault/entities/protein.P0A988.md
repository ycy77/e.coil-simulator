---
entity_id: "protein.P0A988"
entity_type: "protein"
name: "dnaN"
source_database: "UniProt"
source_id: "P0A988"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:23994470}. Note=Localizes to midcell position when chromosomes are condensed during DNA replication (PubMed:23994470). {ECO:0000269|PubMed:23994470}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dnaN b3701 JW3678"
---

# dnaN

`protein.P0A988`

## Static

- Type: `protein`
- Source: `UniProt:P0A988`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:23994470}. Note=Localizes to midcell position when chromosomes are condensed during DNA replication (PubMed:23994470). {ECO:0000269|PubMed:23994470}.

## Enriched Summary

FUNCTION: Confers DNA tethering and processivity to DNA polymerases and other proteins. Acts as a clamp, forming a ring around DNA (a reaction catalyzed by the clamp-loading complex) which diffuses in an ATP-independent manner freely and bidirectionally along dsDNA (PubMed:2040637). DNA bound in the ring is bent 22 degrees, in solution primed DNA is bound more tightly than dsDNA, suggesting the clamp binds both ss- and dsDNA (PubMed:18191219). In a complex of DNA with this protein, alpha, epsilon and tau subunits however the DNA is only slightly bent (PubMed:26499492). Coordinates protein traffic at the replication fork, where it interacts with multiple DNA polymerases, repair factors and other proteins (PubMed:14592985, PubMed:14729336, PubMed:15466025, PubMed:15952889, PubMed:16168375, PubMed:22716942, PubMed:26499492). Initially characterized for its ability to contact the alpha subunit (dnaE) of DNA polymerase III (Pol III), tethering it to the DNA and conferring very high processivity (PubMed:2040637). Pol III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria; it also exhibits 3'-5' exonuclease proofreading activity. The beta chain is required for initiation of replication as well as for processivity of DNA replication (PubMed:2040637, PubMed:3519609)...

## Biological Role

Catalyzes deoxyadenosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00375), deoxyguanosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00376), deoxycytidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00377), deoxythymidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00378), deoxynucleoside triphosphate:DNA deoxynucleotidyltransferase (reaction.R00379). Component of Hda-β-clamp complex (complex.ecocyc.CPLX0-10342), replisome (complex.ecocyc.CPLX0-13320), β sliding clamp (complex.ecocyc.CPLX0-3761), DNA polymerase III, holoenzyme (complex.ecocyc.CPLX0-3803).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: Confers DNA tethering and processivity to DNA polymerases and other proteins. Acts as a clamp, forming a ring around DNA (a reaction catalyzed by the clamp-loading complex) which diffuses in an ATP-independent manner freely and bidirectionally along dsDNA (PubMed:2040637). DNA bound in the ring is bent 22 degrees, in solution primed DNA is bound more tightly than dsDNA, suggesting the clamp binds both ss- and dsDNA (PubMed:18191219). In a complex of DNA with this protein, alpha, epsilon and tau subunits however the DNA is only slightly bent (PubMed:26499492). Coordinates protein traffic at the replication fork, where it interacts with multiple DNA polymerases, repair factors and other proteins (PubMed:14592985, PubMed:14729336, PubMed:15466025, PubMed:15952889, PubMed:16168375, PubMed:22716942, PubMed:26499492). Initially characterized for its ability to contact the alpha subunit (dnaE) of DNA polymerase III (Pol III), tethering it to the DNA and conferring very high processivity (PubMed:2040637). Pol III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria; it also exhibits 3'-5' exonuclease proofreading activity. The beta chain is required for initiation of replication as well as for processivity of DNA replication (PubMed:2040637, PubMed:3519609). A single clamp can bind both Pol III and IV, allowing the repair Pol IV to access DNA when it is damaged and needs to be fixed, a process the replicative polymerase cannot perform; when DNA is repaired Pol III takes over again (PubMed:16168375). Serves as a processivity factor for DNA polymerases II (PubMed:1999435, PubMed:1534562), IV (PubMed:10801133) and V (PubMed:10801133). A shorter protein beta* may be important for increasing survival after UV irradiation, and stimulates DNA synthesis with increased processivity in the presence of core Pol III plus the clamp loader complex (PubMed:8576210, PubMed:8576212). {ECO:0000269|PubMed:10801133, ECO:0000269|PubMed:14592985, ECO:0000269|PubMed:14729336, ECO:0000269|PubMed:1534562, ECO:0000269|PubMed:15466025, ECO:0000269|PubMed:16168375, ECO:0000269|PubMed:18191219, ECO:0000269|PubMed:1999435, ECO:0000269|PubMed:2040637, ECO:0000269|PubMed:22716942, ECO:0000269|PubMed:26499492, ECO:0000269|PubMed:3519609, ECO:0000269|PubMed:8576210, ECO:0000269|PubMed:8576212, ECO:0000305|PubMed:15952889}.; FUNCTION: Required for DnaA inactivation. The RIDA complex (regulatory inactivation of DnaA), composed of ATP-DnaA, Hda and the DNA-loaded beta sliding clamp (this protein) rapidly hydrolyzes ATP-DnaA to ADP-DnaA in a DNA-dependent fashion, preventing reinitiation of DNA replication (PubMed:9674428). DnaA inactivation is stimulated by DNA synthesis (PubMed:9674428). {ECO:0000269|PubMed:9674428}.

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
- `is_component_of` --> [[complex.ecocyc.CPLX0-10342|complex.ecocyc.CPLX0-10342]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-13320|complex.ecocyc.CPLX0-13320]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4
- `is_component_of` --> [[complex.ecocyc.CPLX0-3761|complex.ecocyc.CPLX0-3761]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-3803|complex.ecocyc.CPLX0-3803]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3701|gene.b3701]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A988`
- `KEGG:ecj:JW3678;eco:b3701;ecoc:C3026_20065;`
- `GeneID:93778442;948218;`
- `GO:GO:0003677; GO:0003887; GO:0005829; GO:0006261; GO:0006271; GO:0006974; GO:0008408; GO:0009360; GO:0030174; GO:0030894; GO:0032297; GO:0042276; GO:0042802; GO:0042803; GO:0044787; GO:1990078; GO:1990085`

## Notes

Beta sliding clamp (Beta clamp) (Sliding clamp) (Beta-clamp processivity factor) (DNA polymerase III beta sliding clamp subunit)
