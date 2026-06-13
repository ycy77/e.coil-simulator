---
entity_id: "molecule.C00046"
entity_type: "small_molecule"
name: "RNA"
source_database: "KEGG"
source_id: "C00046"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "RNA"
  - "RNAn"
  - "RNAn+1"
  - "RNA(linear)"
  - "(Ribonucleotide)n"
  - "(Ribonucleotide)m"
  - "(Ribonucleotide)n+m"
  - "Ribonucleic acid"
---

# RNA

`molecule.C00046`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00046`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: RNA; RNAn; RNAn+1; RNA(linear); (Ribonucleotide)n; (Ribonucleotide)m; (Ribonucleotide)n+m; Ribonucleic acid EcoCyc common name: a ribonucleic acid. This class stands for general RNA substrates, to be used in general reactions such as RNA modification. It is not the same as the super class RNAs RNAs, which includes all RNAs in the database.

## Biological Role

Consumed as substrate in 16 reaction(s). Produced in 18 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: RNA; RNAn; RNAn+1; RNA(linear); (Ribonucleotide)n; (Ribonucleotide)m; (Ribonucleotide)n+m; Ribonucleic acid

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (34)

- `is_product_of` --> [[reaction.R00435|reaction.R00435]] `KEGG` `database` - C00002 + C00046 <=> C00013 + C00046
- `is_product_of` --> [[reaction.R00437|reaction.R00437]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00008
- `is_product_of` --> [[reaction.R00438|reaction.R00438]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00015
- `is_product_of` --> [[reaction.R00439|reaction.R00439]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00035
- `is_product_of` --> [[reaction.R00440|reaction.R00440]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00112
- `is_product_of` --> [[reaction.R00441|reaction.R00441]] `KEGG` `database` - C00044 + C00046 <=> C00013 + C00046
- `is_product_of` --> [[reaction.R00442|reaction.R00442]] `KEGG` `database` - C00063 + C00046 <=> C00013 + C00046
- `is_product_of` --> [[reaction.R00443|reaction.R00443]] `KEGG` `database` - C00075 + C00046 <=> C00013 + C00046
- `is_product_of` --> [[reaction.R00444|reaction.R00444]] `KEGG` `database` - C00201 + C00046 <=> C00013 + C00046
- `is_product_of` --> [[reaction.R07282|reaction.R07282]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00454
- `is_product_of` --> [[reaction.ecocyc.DNA-DIRECTED-RNA-POLYMERASE-RXN|reaction.ecocyc.DNA-DIRECTED-RNA-POLYMERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.POLYNUCLEOTIDE-ADENYLYLTRANSFERASE-RXN|reaction.ecocyc.POLYNUCLEOTIDE-ADENYLYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17905|reaction.ecocyc.RXN-17905]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17910|reaction.ecocyc.RXN-17910]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-4223|reaction.ecocyc.RXN0-4223]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6566|reaction.ecocyc.RXN0-6566]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7388|reaction.ecocyc.RXN0-7388]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRNA-NUCLEOTIDYLTRANSFERASE-RXN|reaction.ecocyc.TRNA-NUCLEOTIDYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00435|reaction.R00435]] `KEGG` `database` - C00002 + C00046 <=> C00013 + C00046
- `is_substrate_of` --> [[reaction.R00437|reaction.R00437]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00008
- `is_substrate_of` --> [[reaction.R00438|reaction.R00438]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00015
- `is_substrate_of` --> [[reaction.R00439|reaction.R00439]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00035
- `is_substrate_of` --> [[reaction.R00440|reaction.R00440]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00112
- `is_substrate_of` --> [[reaction.R00441|reaction.R00441]] `KEGG` `database` - C00044 + C00046 <=> C00013 + C00046
- `is_substrate_of` --> [[reaction.R00442|reaction.R00442]] `KEGG` `database` - C00063 + C00046 <=> C00013 + C00046
- `is_substrate_of` --> [[reaction.R00443|reaction.R00443]] `KEGG` `database` - C00075 + C00046 <=> C00013 + C00046
- `is_substrate_of` --> [[reaction.R00444|reaction.R00444]] `KEGG` `database` - C00201 + C00046 <=> C00013 + C00046
- `is_substrate_of` --> [[reaction.R07282|reaction.R07282]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00454
- `is_substrate_of` --> [[reaction.ecocyc.3.1.27.5-RXN|reaction.ecocyc.3.1.27.5-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DNA-DIRECTED-RNA-POLYMERASE-RXN|reaction.ecocyc.DNA-DIRECTED-RNA-POLYMERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.POLYNUCLEOTIDE-ADENYLYLTRANSFERASE-RXN|reaction.ecocyc.POLYNUCLEOTIDE-ADENYLYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19924|reaction.ecocyc.RXN-19924]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4223|reaction.ecocyc.RXN0-4223]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRNA-NUCLEOTIDYLTRANSFERASE-RXN|reaction.ecocyc.TRNA-NUCLEOTIDYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00046`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
