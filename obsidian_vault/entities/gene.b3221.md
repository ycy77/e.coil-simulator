---
entity_id: "gene.b3221"
entity_type: "gene"
name: "nanQ"
source_database: "NCBI RefSeq"
source_id: "gene-b3221"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3221"
  - "nanQ"
---

# nanQ

`gene.b3221`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3221`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nanQ (gene.b3221) is a gene entity. It encodes nanQ (protein.P45424). Encoded protein function: FUNCTION: Opens both the alpha- and beta-forms of N-acetylneuraminate (sialic acid; Neu5Ac) to provide aceneuramate, the preferred substrate for NanA. Has preferential activity on the beta-anomer rather than the alpha-anomer. Accelerates a reaction that is spontaneous at slightly alkaline pH, facilitates the reaction at acidic pH. {ECO:0000269|PubMed:33895133}. EcoCyc product frame: G7675-MONOMER. EcoCyc synonyms: yhcH. Genomic coordinates: 3369014-3369478. EcoCyc protein note: NanQ catalyzes the conversion of N-acetylneuraminate (Neu5Ac) from its cyclic forms to its linear (aldehydo) form. It preferentially acts on the β anomer, which is also the most prevalent form of Neu5Ac in solution. Addition of NanQ increases the activity of ACNEULY-MONOMER in vitro, suggesting that linear Neu5Ac is not a tightly bound intermediate in the NanQ catalytic cycle . Purified NanQ was found to contain Zn2+. Zn2+ and other divalent cations themselves increase the rate of formation of the linear form of Neu5Ac, albeit at non-physiological concentrations. The Zn2+ contained in NanQ could therefore play a catalytic role...

## Biological Role

Repressed by fis (protein.P0A6R3), nanR (protein.P0A8W0). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45424|protein.P45424]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=nanQ; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nanQ; function=-
- `represses` <-- [[protein.P0A8W0|protein.P0A8W0]] `RegulonDB` `C` - regulator=NanR; target=nanQ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010569,ECOCYC:G7675,GeneID:947750`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3369014-3369478:-; feature_type=gene
