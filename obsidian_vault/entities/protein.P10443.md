---
entity_id: "protein.P10443"
entity_type: "protein"
name: "dnaE"
source_database: "UniProt"
source_id: "P10443"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dnaE polC b0184 JW0179"
---

# dnaE

`protein.P10443`

## Static

- Type: `protein`
- Source: `UniProt:P10443`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria (PubMed:2932432). This DNA polymerase also exhibits 3' to 5' exonuclease activity. The alpha chain is the DNA polymerase catalytic subunit (PubMed:2932432). It is tethered to replicating DNA by the beta sliding clamp (dnaN), which confers extremely high processivity to the catalytic subunit, copying a 5.4 kb genome in 11 seconds, a speed of at least 500 nucleotides/second at 30 degrees Celsius (PubMed:2413035). {ECO:0000269|PubMed:2413035, ECO:0000269|PubMed:2932432}. The alpha subunit of DNA polymerase III catalyzes the polymerase activity of the holoenzyme complex . Replicative 5' to 3' polymerization of DNA requires dNTPs and template DNA with a bound RNA primer . The newly polymerized DNA is covalently attached to the RNA primer . The presence of the epsilon subunit increases the polymerase activity of the alpha subunit two-fold . The alpha subunit is required for misincorporation and bypass during UV mutagenesis . The middle portion of the alpha subunit (residues 542-991) is involved in binding to the polymerase III beta subunit. Deletion of the amino-terminal portion of alpha (residues 1-542) actually increases its affinity for beta . The carboxy-terminus of alpha is required for binding to the polymerase III tau subunit...

## Biological Role

Catalyzes deoxyadenosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00375), deoxyguanosine 5'-triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00376), deoxycytidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00377), deoxythymidine triphosphate:DNA deoxynucleotidyltransferase (DNA-directed) (reaction.R00378), deoxynucleoside triphosphate:DNA deoxynucleotidyltransferase (reaction.R00379), DNA-DIRECTED-DNA-POLYMERASE-RXN (reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN). Component of replisome (complex.ecocyc.CPLX0-13320), DNA polymerase III, core enzyme (complex.ecocyc.CPLX0-2361), DNA polymerase III, holoenzyme (complex.ecocyc.CPLX0-3803). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria (PubMed:2932432). This DNA polymerase also exhibits 3' to 5' exonuclease activity. The alpha chain is the DNA polymerase catalytic subunit (PubMed:2932432). It is tethered to replicating DNA by the beta sliding clamp (dnaN), which confers extremely high processivity to the catalytic subunit, copying a 5.4 kb genome in 11 seconds, a speed of at least 500 nucleotides/second at 30 degrees Celsius (PubMed:2413035). {ECO:0000269|PubMed:2413035, ECO:0000269|PubMed:2932432}.

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
- `catalyzes` --> [[reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN|reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-13320|complex.ecocyc.CPLX0-13320]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.CPLX0-2361|complex.ecocyc.CPLX0-2361]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-3803|complex.ecocyc.CPLX0-3803]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0184|gene.b0184]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10443`
- `KEGG:ecj:JW0179;eco:b0184;ecoc:C3026_00845;`
- `GeneID:944877;`
- `GO:GO:0003677; GO:0003887; GO:0005737; GO:0005829; GO:0006261; GO:0006272; GO:0006273; GO:0009360; GO:0030894; GO:0044776`
- `EC:2.7.7.7`

## Notes

DNA polymerase III subunit alpha (EC 2.7.7.7)
