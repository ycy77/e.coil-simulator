---
entity_id: "gene.b0047"
entity_type: "gene"
name: "kefC"
source_database: "NCBI RefSeq"
source_id: "gene-b0047"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0047"
  - "kefC"
---

# kefC

`gene.b0047`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0047`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kefC (gene.b0047) is a gene entity. It encodes kefC (protein.P03819). Encoded protein function: FUNCTION: Pore-forming subunit of a potassium efflux system that confers protection against electrophiles. Catalyzes K(+)/H(+) antiport. Can also export rubidium, lithium and sodium. {ECO:0000255|HAMAP-Rule:MF_01413, ECO:0000269|PubMed:17679694, ECO:0000269|PubMed:21041667, ECO:0000269|PubMed:9023177}. EcoCyc product frame: KEFC-MONOMER. EcoCyc synonyms: trkC. Genomic coordinates: 47769-49631. EcoCyc protein note: KefB and KefC are two independent glutathione-regulated potassium efflux systems, which play a role in protecting the cell from electrophile toxicity. Mutations in kefB and kefC affect potassium efflux at neutral pH, can be complemented by the cloned genes and probably function via potassium/proton antiport . Potassium efflux by KefB or KefC is activated by adducts formed by reaction of glutathione with electrophilic compounds such as N-ethylmaleimide, methylglyoxal and chlorodinitrobenzene . Potassium efflux mediated by KefB and KefC leads to acidification of the cytoplasm, which protects the cell from electrophile toxicity . KefB and KefC differ in their activation by methylglyoxal, with KefC only weakly activated . KefC is a member of the CPA2 family of monovalent cation/proton antiporters. The ancillary protein, KefF, is required for maximum activity of KefC...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03819|protein.P03819]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000161,ECOCYC:EG10521,GeneID:944773`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:47769-49631:+; feature_type=gene
