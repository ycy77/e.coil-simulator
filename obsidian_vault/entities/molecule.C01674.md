---
entity_id: "molecule.C01674"
entity_type: "small_molecule"
name: "Chitobiose"
source_database: "KEGG"
source_id: "C01674"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Chitobiose"
  - "Diacetylchitobiose"
  - "N,N'-Diacetylchitobiose"
  - "β-D-glucosaminyl-(1→4)-D-glucosamine"
  - "2-amino-4-O-(2-amino-2-deoxy-β-D-glucopyranosyl)-2-deoxy-D-glucopyranose"
---

# Chitobiose

`molecule.C01674`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01674`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Chitobiose; Diacetylchitobiose; N,N'-Diacetylchitobiose EcoCyc common name: N,N'-diacetylchitobiose. There is some ambiguity in the literature as to the identity of CPD-13545 regarding acetylation. Although CHITIN consists of β(1→4) linked N-acetylglucosamine residues, the name chitobiose was given to the parent non-acetylated disaccharide by analogy with CPD-15975 cellobiose, the repeating disaccharide from CELLULOSE. Thus the name chitobiose is used for the disaccharide that contains non-acetylated glucosamine residues. The acetylated forms are referred to as CPD-12274 and CHITOBIOSE

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: Chitobiose; Diacetylchitobiose; N,N'-Diacetylchitobiose

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R02334|reaction.R02334]] `KEGG` `database` - C00461 + C00001 <=> C01674 + C00461
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-445|reaction.ecocyc.TRANS-RXN0-445]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00022|reaction.R00022]] `KEGG` `database` - C01674 + C00001 <=> 2 C00140
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-155B|reaction.ecocyc.TRANS-RXN-155B]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-445|reaction.ecocyc.TRANS-RXN0-445]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01674`
- `EcoCyc:CPD-13545`
- `PUBCHEM:146037260`
- `SEED:cpd23928`
- `METANETX:MNXM13289`
- `CHEBI:50675`
- `canonicalized_from:molecule.ecocyc.CPD-13545`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.CPD-13545: EcoCyc:CPD-13545
