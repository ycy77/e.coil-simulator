---
entity_id: "gene.b1335"
entity_type: "gene"
name: "ogt"
source_database: "NCBI RefSeq"
source_id: "gene-b1335"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1335"
  - "ogt"
---

# ogt

`gene.b1335`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1335`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ogt (gene.b1335) is a gene entity. It encodes ogt (protein.P0AFH0). Encoded protein function: FUNCTION: Involved in the cellular defense against the biological effects of O6-methylguanine (O6-MeG) and O4-methylthymine (O4-MeT) in DNA. Repairs the methylated nucleobase in DNA by stoichiometrically transferring the methyl group to a cysteine residue in the enzyme. This is a suicide reaction: the enzyme is irreversibly inactivated. EcoCyc product frame: EG10668-MONOMER. Genomic coordinates: 1399721-1400236. EcoCyc protein note: Ogt is the second (after PD00230 "Ada") methyltransferase enzyme for the direct repair of alkylated DNA in Escherichia coli. The enzyme (characterized initially in E. coli B) repairs alkylated DNA (O6-methylguanine, O4-methylthymine, and O6-ethylguanine lesions) by irreversibly transferring the alkyl group to its own cysteine residue (Cys-139); it does not repair methylphosphotriesters, is not inducible and and does not trigger the adaptive response to alkylating agents . Ogt repairs O4-methylthymine lesions more effectively than O6-methylguanine in vitro . Cell extracts from a strain lacking both Ada and Ogt (Δada ogt-1::Kan) show no methyltransferase activity; Ogt is the only constitutively expressed O6-methylguanine DNA methyltransferase in E...

## Biological Role

Repressed by fis (protein.P0A6R3). Activated by narL (protein.P0AF28).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFH0|protein.P0AFH0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=ogt; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=ogt; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004486,ECOCYC:EG10668,GeneID:945853`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1399721-1400236:-; feature_type=gene
