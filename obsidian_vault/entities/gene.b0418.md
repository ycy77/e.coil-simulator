---
entity_id: "gene.b0418"
entity_type: "gene"
name: "pgpA"
source_database: "NCBI RefSeq"
source_id: "gene-b0418"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0418"
  - "pgpA"
---

# pgpA

`gene.b0418`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0418`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pgpA (gene.b0418) is a gene entity. It encodes pgpA (protein.P18200). Encoded protein function: FUNCTION: Lipid phosphatase which dephosphorylates phosphatidylglycerophosphate (PGP) to phosphatidylglycerol (PG). {ECO:0000269|PubMed:20485265, ECO:0000269|PubMed:21148555, ECO:0000269|PubMed:2846510, ECO:0000269|PubMed:6296050}. EcoCyc product frame: PGPPHOSPHAA-MONOMER. EcoCyc synonyms: yajN. Genomic coordinates: 436589-437107. EcoCyc protein note: E.coli contains three phosphatidylglycerophosphatases - PgpA, PGPPHOSPHAB-MONOMER "PgpB" and EG11371 "PgpC" - which catalyse the dephosphorylation of phosphatidylglycerol phosphate (PGP) to phosphatidylglycerol (PG), an essential phospholipid of the inner and outer membrane in E. coli. PgpA and PgpC appear to be specific for PGP whereas PgpB is a multifunctional enzyme that is also active on undecaprenyl diphosphate, phosphatidicic acid and lysophosphatidic acid . A pgpApgpBpgpC triple mutant is not viable but can be generated with a complementing plasmid containing any one of the three phosphatidylglycerophosphatases. A triple mutant complemented with any one of pgpA, pgpB or pgpC expressed on a temperature sensitive plasmid is viable at 30°C but not at 42°C . Lipid profiling of these strains showed accumulation of PGP and disappearance of PG when shifted from 30°C to 42°C...

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P18200|protein.P18200]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=pgpA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001454,ECOCYC:EG10704,GeneID:947542`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:436589-437107:+; feature_type=gene
