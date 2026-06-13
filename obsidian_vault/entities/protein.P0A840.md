---
entity_id: "protein.P0A840"
entity_type: "protein"
name: "surE"
source_database: "UniProt"
source_id: "P0A840"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "surE ygbC b2744 JW2714"
---

# surE

`protein.P0A840`

## Static

- Type: `protein`
- Source: `UniProt:P0A840`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Nucleotidase with a broad substrate specificity as it can dephosphorylate various ribo- and deoxyribonucleoside 5'-monophosphates and ribonucleoside 3'-monophosphates with highest affinity to 3'-AMP (PubMed:15489502). Also hydrolyzes polyphosphate (exopolyphosphatase activity) with the preference for short-chain-length substrates (P20-25) (PubMed:15489502). Might be involved in the regulation of dNTP and NTP pools, and in the turnover of 3'-mononucleotides produced by numerous intracellular RNases (T1, T2, and F) during the degradation of various RNAs (PubMed:15489502). Also plays a significant physiological role in stress-response and is required for the survival of E.coli in stationary growth phase (PubMed:15489502). {ECO:0000269|PubMed:15489502, ECO:0000303|PubMed:15489502}. UmpG (SurE) is a phosphatase with broad substrate specificity. It efficiently hydrolyzes purine and pyrimidine ribonucleotides and deoxyribonucleotides, and polyphosphate. UmpG and its homologs are widely distributed among bacteria, archaea and eukaryotes . The enzyme was found to participate in the degradation of "overflow" UMP nucleotides . UmpG hydrolyzes purine and pyrimidine ribonucleotides and deoxyribonucleotides, as well as the synthetic substrate p-nitrophenyl phosphate, with pH optima of 7.0-7.2. A divalent metal cation is required and Mn2+, Co2+, Mg2+ or Ni2+ are effective...

## Biological Role

Catalyzes adenosine 5'-monophosphate phosphohydrolase (reaction.R00183), cytidine-5'-monophosphate phosphohydrolase (reaction.R00511), uridine 3'-monophosphate phosphohydrolase (reaction.R01877), cytidine 3'-phosphate phosphohydrolase (reaction.R02370), 3-NUCLEOTID-RXN (reaction.ecocyc.3-NUCLEOTID-RXN), 5-NUCLEOTID-RXN (reaction.ecocyc.5-NUCLEOTID-RXN), RXN-14090 (reaction.ecocyc.RXN-14090), RXN-14126 (reaction.ecocyc.RXN-14126), and 1 more. Bound by Cobalt ion (molecule.C00175), Magnesium cation (molecule.C00305), Nickel(2+) (molecule.C19609), Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Nucleotidase with a broad substrate specificity as it can dephosphorylate various ribo- and deoxyribonucleoside 5'-monophosphates and ribonucleoside 3'-monophosphates with highest affinity to 3'-AMP (PubMed:15489502). Also hydrolyzes polyphosphate (exopolyphosphatase activity) with the preference for short-chain-length substrates (P20-25) (PubMed:15489502). Might be involved in the regulation of dNTP and NTP pools, and in the turnover of 3'-mononucleotides produced by numerous intracellular RNases (T1, T2, and F) during the degradation of various RNAs (PubMed:15489502). Also plays a significant physiological role in stress-response and is required for the survival of E.coli in stationary growth phase (PubMed:15489502). {ECO:0000269|PubMed:15489502, ECO:0000303|PubMed:15489502}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (9)

- `catalyzes` --> [[reaction.R00183|reaction.R00183]] `KEGG` `database` - via EC:3.1.3.5
- `catalyzes` --> [[reaction.R00511|reaction.R00511]] `KEGG` `database` - via EC:3.1.3.5
- `catalyzes` --> [[reaction.R01877|reaction.R01877]] `KEGG` `database` - via EC:3.1.3.6
- `catalyzes` --> [[reaction.R02370|reaction.R02370]] `KEGG` `database` - via EC:3.1.3.6
- `catalyzes` --> [[reaction.ecocyc.3-NUCLEOTID-RXN|reaction.ecocyc.3-NUCLEOTID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.5-NUCLEOTID-RXN|reaction.ecocyc.5-NUCLEOTID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14090|reaction.ecocyc.RXN-14090]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14126|reaction.ecocyc.RXN-14126]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14142|reaction.ecocyc.RXN-14142]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2744|gene.b2744]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A840`
- `KEGG:ecj:JW2714;eco:b2744;ecoc:C3026_15090;`
- `GeneID:93779262;947211;`
- `GO:GO:0000166; GO:0004309; GO:0005737; GO:0008253; GO:0008254; GO:0030145; GO:0046050`
- `EC:3.1.3.5; 3.1.3.6; 3.6.1.11`

## Notes

5'/3'-nucleotidase SurE (EC 3.1.3.5) (EC 3.1.3.6) (Exopolyphosphatase) (EC 3.6.1.11) (Nucleoside monophosphate phosphohydrolase) (Stationary-phase survival protein SurE)
