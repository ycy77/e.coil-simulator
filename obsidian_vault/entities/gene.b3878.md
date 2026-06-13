---
entity_id: "gene.b3878"
entity_type: "gene"
name: "yihQ"
source_database: "NCBI RefSeq"
source_id: "gene-b3878"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3878"
  - "yihQ"
---

# yihQ

`gene.b3878`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3878`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yihQ (gene.b3878) is a gene entity. It encodes yihQ (protein.P32138). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of sulfoquinovosyl diacylglycerides (SQDG) to sulfoquinovose (SQ), which is then degraded by E.coli through the SQ Embden-Meyerhof-Parnas (SQ-EMP) sulfoglycolysis pathway as a source of carbon and sulfur. Therefore, is likely involved in the utilization of the sulfoquinovose headgroup found in ubiquitous plant sulfolipids (PubMed:26878550). Is also able to hydrolyze simple sulfoquinovosides such as sulfoquinovosyl glycerol (SQGro) (PubMed:26878550, PubMed:30276262). In vitro, can use the substrate analog para-nitrophenyl alpha-sulfoquinovoside (PNPSQ), but shows no detectable activity toward 4-nitrophenyl alpha-D-glucopyranoside (PNPGlc) (PubMed:26878550, PubMed:30276262). Is a retaining glycoside hydrolase, since it forms the alpha anomer of SQ (PubMed:26878550). Also exhibits some alpha-glucosidase activity against alpha-glucosyl fluoride in vitro, although natural substrates, such as alpha-glucobioses are scarcely hydrolyzed (PubMed:15294295). {ECO:0000269|PubMed:15294295, ECO:0000269|PubMed:26878550, ECO:0000269|PubMed:30276262}. EcoCyc product frame: EG11843-MONOMER. EcoCyc synonyms: squQ. Genomic coordinates: 4067240-4069276...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32138|protein.P32138]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yihQ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012666,ECOCYC:EG11843,GeneID:948376`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4067240-4069276:-; feature_type=gene
