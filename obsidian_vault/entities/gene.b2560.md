---
entity_id: "gene.b2560"
entity_type: "gene"
name: "pgpC"
source_database: "NCBI RefSeq"
source_id: "gene-b2560"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2560"
  - "pgpC"
---

# pgpC

`gene.b2560`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2560`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pgpC (gene.b2560) is a gene entity. It encodes pgpC (protein.P0AD42). Encoded protein function: FUNCTION: Lipid phosphatase which dephosphorylates phosphatidylglycerophosphate (PGP) to phosphatidylglycerol (PG). {ECO:0000269|PubMed:21148555}. EcoCyc product frame: EG11371-MONOMER. EcoCyc synonyms: yfhB. Genomic coordinates: 2697915-2698550. EcoCyc protein note: E.coli contains three phosphatidylglycerophosphatases - EG10704 "PgpA", PGPPHOSPHAB-MONOMER "PgpB" and PgpC - which catalyse the dephosphorylation of phosphatidylglycerol phosphate (PGP) to phosphatidylglycerol (PG), an essential phospholipid of the inner and outer membrane in E. coli. PgpA and PgpC appear to be specific for PGP whereas PgpB is a multifunctional enzyme that is also active on undecaprenyl diphosphate, phosphatidicic acid and lysophosphatidic acid . pgpC is essential for growth in a pgpApgpB mutant but not in wild type cells . A pgpApgpBpgpC triple mutant is not viable but can be generated with a complementing plasmid containing any one of the three phosphatidylglycerophosphatases. A triple mutant complemented with any one of pgpA, pgpB or pgpC expressed on a temperature sensitive plasmid is viable at 30°C but not at 42°C . Lipid profiling of these strains showed accumulation of PGP and disappearance of PG when shifted from 30°C to 42°C...

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD42|protein.P0AD42]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008421,ECOCYC:EG11371,GeneID:947026`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2697915-2698550:-; feature_type=gene
