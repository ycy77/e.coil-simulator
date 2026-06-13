---
entity_id: "gene.b0463"
entity_type: "gene"
name: "acrA"
source_database: "NCBI RefSeq"
source_id: "gene-b0463"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0463"
  - "acrA"
---

# acrA

`gene.b0463`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0463`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

acrA (gene.b0463) is a gene entity. It encodes acrA (protein.P0AE06). Encoded protein function: FUNCTION: Periplasmic adaptor component of the AcrAB-TolC efflux system that confers multidrug resistance (PubMed:9878415). The AcrAB-TolC efflux system has a broad substrate specificity, acting as a substrate:proton antiporter, using proton motive force to export substrates (Probable). AcrA is elongated in shape, being long enough to span the periplasm, linking AcrB and TolC stably together, perhaps promoted by binding to peptidoglycan (PubMed:22308040, PubMed:9878415). AcrA is also a component of the AcrABZ-TolC efflux system, where the small accessory protein AcrZ, together with membrane lipids, may influence the specificity of drug export (PubMed:23010927, PubMed:28355133). {ECO:0000269|PubMed:22308040, ECO:0000269|PubMed:23010927, ECO:0000269|PubMed:28355133, ECO:0000269|PubMed:9878415, ECO:0000305|PubMed:28355133}. EcoCyc product frame: EG11703-MONOMER. EcoCyc synonyms: sipB, Mb, lir, mbl, mtcA, nbsA. Genomic coordinates: 484426-485619. EcoCyc protein note: AcrA is the periplasmic lipoprotein component of the AcrAB-TolC and AcrAD-TolC multidrug efflux pumps...

## Biological Role

Repressed by acrR (protein.P0ACS9), envR (protein.P0ACT2). Activated by soxS (protein.P0A9E2), marA (protein.P0ACH5), rob (protein.P0ACI0).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE06|protein.P0AE06]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=acrA; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=acrA; function=+
- `activates` <-- [[protein.P0ACI0|protein.P0ACI0]] `RegulonDB` `S` - regulator=Rob; target=acrA; function=+
- `represses` <-- [[protein.P0ACS9|protein.P0ACS9]] `RegulonDB` `C` - regulator=AcrR; target=acrA; function=-
- `represses` <-- [[protein.P0ACT2|protein.P0ACT2]] `RegulonDB` `S` - regulator=EnvR; target=acrA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001603,ECOCYC:EG11703,GeneID:945112`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:484426-485619:-; feature_type=gene
