---
entity_id: "gene.b3350"
entity_type: "gene"
name: "kefB"
source_database: "NCBI RefSeq"
source_id: "gene-b3350"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3350"
  - "kefB"
---

# kefB

`gene.b3350`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3350`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kefB (gene.b3350) is a gene entity. It encodes kefB (protein.P45522). Encoded protein function: FUNCTION: Pore-forming subunit of a potassium efflux system that confers protection against electrophiles. Catalyzes K(+)/H(+) antiport. {ECO:0000255|HAMAP-Rule:MF_01412, ECO:0000269|PubMed:3301813, ECO:0000269|PubMed:9023177}. EcoCyc product frame: KEFB-MONOMER. EcoCyc synonyms: trkB. Genomic coordinates: 3478802-3480607. EcoCyc protein note: KefB and KefC are two independent glutathione-regulated potassium efflux systems, which play a role in protecting the cell from electrophile toxicity. Mutations in kefB and kefC affect potassium efflux at neutral pH, can be complemented by the cloned genes and probably function via potassium/proton antiport . Potassium efflux by KefB or KefC is activated by adducts formed by reaction of glutathione with electrophilic compounds such as N-ethylmaleimide, methylglyoxal and chlorodinitrobenzene . Potassium efflux mediated by KefB and KefC leads to acidification of the cytoplasm, which protects the cell from electrophile toxicity . KefB and KefC differ in their activation by methylglyoxal, with KefC only weakly activated . KefB is a member of the CPA2 family of monovalent cation:proton antiporters. In addition to KefB and KefC, additional unidentified potassium efflux systems exist.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45522|protein.P45522]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010949,ECOCYC:EG20110,GeneID:947858`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3478802-3480607:-; feature_type=gene
