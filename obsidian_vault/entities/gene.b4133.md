---
entity_id: "gene.b4133"
entity_type: "gene"
name: "cadC"
source_database: "NCBI RefSeq"
source_id: "gene-b4133"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4133"
  - "cadC"
---

# cadC

`gene.b4133`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4133`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cadC (gene.b4133) is a gene entity. It encodes cadC (protein.P23890). Encoded protein function: FUNCTION: Regulates the lysine- and pH-dependent expression of the lysine decarboxylase CadA and the cadaverine-lysine antiporter CadB (PubMed:1370290, PubMed:16491024, PubMed:18086202, PubMed:21216950). At low external pH, and in the presence of external lysine, CadC activates transcription of the cadBA operon by binding directly to two sites, Cad1 and Cad2, within the cadBA promoter region (Pcad) (PubMed:16491024, PubMed:28432336). Preferentially binds to AT-rich regions within the Cad1 promoter (PubMed:28432336). {ECO:0000269|PubMed:1370290, ECO:0000269|PubMed:16491024, ECO:0000269|PubMed:18086202, ECO:0000269|PubMed:21216950, ECO:0000269|PubMed:28432336}. EcoCyc product frame: PD00436. Genomic coordinates: 4360396-4361934. EcoCyc protein note: CadC is a metal-sensitive transcriptional activator that regulates the expression of genes involved in cadaverine synthesis and excretion under low external pH and high concentrations of lysine . CadC appears to have a modest role in bacterial triclosan resistance . On the other hand, inhibition of cadC expression by CRISPRi reduced cellular fitness under treatment with the antibiotics polymyxin B or puromycin . Two binding sites for CadC, Cad1 and Cad2, have been determined in the cadBA operon...

## Biological Role

Repressed by ompR (protein.P0AA16), hns (protein.P0ACF8). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), mlrA (protein.P33358), glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23890|protein.P23890]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=cadC; function=+
- `activates` <-- [[protein.P33358|protein.P33358]] `RegulonDB` `S` - regulator=MlrA; target=cadC; function=+
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=cadC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=cadC; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=cadC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013532,ECOCYC:EG10133,GeneID:948653`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4360396-4361934:-; feature_type=gene
