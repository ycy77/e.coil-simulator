---
entity_id: "gene.b1095"
entity_type: "gene"
name: "fabF"
source_database: "NCBI RefSeq"
source_id: "gene-b1095"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1095"
  - "fabF"
---

# fabF

`gene.b1095`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1095`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fabF (gene.b1095) is a gene entity. It encodes fabF (protein.P0AAI5). Encoded protein function: FUNCTION: Involved in the type II fatty acid elongation cycle (PubMed:6988423, PubMed:9013860). Catalyzes the elongation of a wide range of acyl-ACP by the addition of two carbons from malonyl-ACP to an acyl acceptor (PubMed:22017312, PubMed:9013860). Can efficiently catalyze the conversion of palmitoleoyl-ACP (cis-hexadec-9-enoyl-ACP) to cis-vaccenoyl-ACP (cis-octadec-11-enoyl-ACP), an essential step in the thermal regulation of fatty acid composition (PubMed:6988423, PubMed:9013860). Can use acyl chains from C-6 to C-16 (PubMed:22017312, PubMed:9013860). Is able to catalyze the condensation reaction when CoA is the carrier for both substrates (PubMed:22017312). {ECO:0000269|PubMed:22017312, ECO:0000269|PubMed:6988423, ECO:0000269|PubMed:9013860}. EcoCyc product frame: 3-OXOACYL-ACP-SYNTHII-MONOMER. EcoCyc synonyms: vtr, cvc, fabJ, vtrB. Genomic coordinates: 1151939-1153180.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAI5|protein.P0AAI5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fabF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003705,ECOCYC:EG12606,GeneID:946665`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1151939-1153180:+; feature_type=gene
