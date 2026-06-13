---
entity_id: "gene.b3781"
entity_type: "gene"
name: "trxA"
source_database: "NCBI RefSeq"
source_id: "gene-b3781"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3781"
  - "trxA"
---

# trxA

`gene.b3781`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3781`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trxA (gene.b3781) is a gene entity. It encodes trxA (protein.P0AA25). Encoded protein function: FUNCTION: Participates in various redox reactions through the reversible oxidation of its active center dithiol to a disulfide and catalyzes dithiol-disulfide exchange reactions. EcoCyc product frame: OX-THIOREDOXIN-MONOMER. EcoCyc synonyms: dasC, fipA, tsnC. Genomic coordinates: 3965761-3966090. EcoCyc protein note: Represents the oxidized form of RED-THIOREDOXIN-MONOMER. EcoCyc protein note: Thioredoxins are small electron transfer proteins that contain a cysteine disulfide/dithiol active site with the amino acid sequence motif Cys-X-X-Cys (where X is any amino acid). They are members of the thioredoxin protein family. Members of this family/superfamily contain the thioredoxin fold, a characteristic and stable protein fold consisting of four β-sheets surrounded by three α-helices (reviewed in ). The proteins function in a wide variety of cellular processes. Thioredoxin is reduced by NADPH in a reaction catalyzed by thioredoxin reductase. The conversion between the oxidized and reduced forms results in a subtle change of conformation. The functional properties differ between the two forms of thioredoxin. The reduced form of thioredoxin is a protein disulfide reductase, and catalyzes dithiol-disulfide exchange reactions...

## Biological Role

Repressed by crp (protein.P0ACJ8). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA25|protein.P0AA25]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=trxA; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=trxA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012357,ECOCYC:EG11031,GeneID:948289`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3965761-3966090:+; feature_type=gene
