---
entity_id: "gene.b2213"
entity_type: "gene"
name: "ada"
source_database: "NCBI RefSeq"
source_id: "gene-b2213"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2213"
  - "ada"
---

# ada

`gene.b2213`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2213`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ada (gene.b2213) is a gene entity. It encodes ada (protein.P06134). Encoded protein function: FUNCTION: Involved in the adaptive response to alkylation damage in DNA caused by alkylating agents. Repairs O6-methylguanine (O6-MeG) and O4-methylthymine (O4-MeT) in DNA. Repairs the methylated nucleobase in DNA by stoichiometrically transferring the methyl group to a cysteine residue in the enzyme (Cys-321). Also specifically repairs the Sp diastereomer of DNA methylphosphotriester lesions by the same mechanism, although the methyl transfer occurs onto a different cysteine residue (Cys-38). Cannot demethylate the other diastereomer, Rp-methylphosphotriester. This is a suicide reaction: the enzyme is irreversibly inactivated. {ECO:0000269|PubMed:2987862}.; FUNCTION: The methylation of Ada by methylphosphotriesters in DNA leads to its activation as a transcriptional regulator that activates the transcription of its own gene, ada, and other alkylation resistance genes, alkA, alkB and aidB. {ECO:0000269|PubMed:2987862}. EcoCyc product frame: PD00230. Genomic coordinates: 2309341-2310405. EcoCyc protein note: ada encodes a bifunctional methyltransferase and transcriptional regulator which is a key component of the adaptive response - the mechanism of adaption induced after exposure to small amounts of DNA alkylating agents...

## Biological Role

Repressed by ada (protein.P06134). Activated by rpoD (protein.P00579), ada (protein.P06134), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06134|protein.P06134]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ada; function=+
- `activates` <-- [[protein.P06134|protein.P06134]] `RegulonDB` `C` - regulator=Ada; target=ada; function=-+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ada; function=+
- `represses` <-- [[protein.P06134|protein.P06134]] `RegulonDB` `C` - regulator=Ada; target=ada; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0007311,ECOCYC:EG10029,GeneID:946710`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2309341-2310405:-; feature_type=gene
