---
entity_id: "gene.b1840"
entity_type: "gene"
name: "yebZ"
source_database: "NCBI RefSeq"
source_id: "gene-b1840"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1840"
  - "yebZ"
---

# yebZ

`gene.b1840`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1840`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yebZ (gene.b1840) is a gene entity. It encodes yebZ (protein.P76278). Encoded protein function: FUNCTION: Component of the AZY copper uptake system (PubMed:40108346). YebZ functions as an energy-dependent copper importer (PubMed:40108346). The AZY proteins link copper import to multiple antibiotic resistance (PubMed:40108346). They are necessary for the copper-dependent activation of the mar operon, thus leading to multidrug antibiotic resistance via the mar pathway (PubMed:40108346). The AZY proteins may also be involved in copper delivery to membrane proteins, but they are not involved in copper tolerance or antioxidant defense (PubMed:34822841). {ECO:0000269|PubMed:34822841, ECO:0000269|PubMed:40108346}. EcoCyc product frame: G7013-MONOMER. Genomic coordinates: 1923719-1924591. EcoCyc protein note: YebZ is a member of the CopD family of copper-sequestering proteins; YebZ is encoded in an operon with the G7014-MONOMER copper-binding protein YobA and a periplasmic protein G7012-MONOMER YebY (the AZY operon); YobA-YebZ-YebY (the AZY proteins) constitute a copper uptake system that is essential for activation of the TU00190 mar operon and for resistance to the antibiotics norfloxacin, ciprofloxacin, and ampicillin . YebZ functions as an energy-dependent copper importer; YebZ activity is enhanced by YobA and diminished by YebY...

## Biological Role

Repressed by nac (protein.Q47005). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76278|protein.P76278]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yebZ; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yebZ; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0006120,ECOCYC:G7013,GeneID:947078`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1923719-1924591:-; feature_type=gene
