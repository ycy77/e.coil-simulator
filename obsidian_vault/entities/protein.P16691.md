---
entity_id: "protein.P16691"
entity_type: "protein"
name: "phnO"
source_database: "UniProt"
source_id: "P16691"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phnO b4093 JW4054"
---

# phnO

`protein.P16691`

## Static

- Type: `protein`
- Source: `UniProt:P16691`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Aminoalkylphosphonate N-acetyltransferase which is able to acetylate a range of aminoalkylphosphonic acids, including aminomethylphosphonate, (S)-1-aminoethylphosphonate and 2-aminoethyl- and 3-aminopropylphosphonate, using acetyl-CoA as acetyl donor. Is required for the utilization of aminomethylphosphonate and (S)-1-aminoethylphosphonate as a phosphate source via the C-P lyase pathway. Is also essential for the detoxification of (S)-1-aminoethylphosphonate, a structural analog of D-alanine that has bacteriocidal properties due to inhibition of cell wall synthesis (PubMed:23056305). Also acts as a N-epsilon-lysine acetyltransferase that catalyzes acetylation of several proteins (PubMed:30352934). {ECO:0000269|PubMed:23056305, ECO:0000269|PubMed:30352934}. PhnO is an aminoalkylphosphonate N-acetyltransferase that is involved in the utilization of aminomethylphosphonate as a source of phosphate. phn+ strains that contain a functional allele of phnE can utilize aminomethylphosphonate (AmMePn), 2-aminoethylphosphonate (2AmEtPn), 3-aminopropylphosphonate (3AmPrPn) as well as methylphosphonate (MePn), ethylphosphonate (EtPn) and propylphosphonate (PrPn) as the source of phosphate. A phnO mutant derivative has lost the ability to utilize AmMePn as the sole source of phosphate, but is still able to utilize the other compounds...

## Biological Role

Catalyzes acetyl-CoA:2-aminoethylphosphonate N-acetyltransferase (reaction.R11479), RXN-17960 (reaction.ecocyc.RXN-17960), RXN-17961 (reaction.ecocyc.RXN-17961), RXN-17962 (reaction.ecocyc.RXN-17962), RXN0-7014 (reaction.ecocyc.RXN0-7014), RXN0-7160 (reaction.ecocyc.RXN0-7160).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)

## Annotation

FUNCTION: Aminoalkylphosphonate N-acetyltransferase which is able to acetylate a range of aminoalkylphosphonic acids, including aminomethylphosphonate, (S)-1-aminoethylphosphonate and 2-aminoethyl- and 3-aminopropylphosphonate, using acetyl-CoA as acetyl donor. Is required for the utilization of aminomethylphosphonate and (S)-1-aminoethylphosphonate as a phosphate source via the C-P lyase pathway. Is also essential for the detoxification of (S)-1-aminoethylphosphonate, a structural analog of D-alanine that has bacteriocidal properties due to inhibition of cell wall synthesis (PubMed:23056305). Also acts as a N-epsilon-lysine acetyltransferase that catalyzes acetylation of several proteins (PubMed:30352934). {ECO:0000269|PubMed:23056305, ECO:0000269|PubMed:30352934}.

## Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.R11479|reaction.R11479]] `KEGG` `database` - via EC:2.3.1.280
- `catalyzes` --> [[reaction.ecocyc.RXN-17960|reaction.ecocyc.RXN-17960]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17961|reaction.ecocyc.RXN-17961]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17962|reaction.ecocyc.RXN-17962]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7014|reaction.ecocyc.RXN0-7014]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7160|reaction.ecocyc.RXN0-7160]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4093|gene.b4093]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16691`
- `KEGG:ecj:JW4054;eco:b4093;ecoc:C3026_22125;`
- `GeneID:75169611;75203244;948599;`
- `GO:GO:0008080; GO:0033051; GO:0061733`
- `EC:2.3.1.-; 2.3.1.280`

## Notes

Aminoalkylphosphonate N-acetyltransferase (EC 2.3.1.280) (KAT) (Peptidyl-lysine N-acetyltransferase) (EC 2.3.1.-)
