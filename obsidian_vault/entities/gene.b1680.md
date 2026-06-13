---
entity_id: "gene.b1680"
entity_type: "gene"
name: "sufS"
source_database: "NCBI RefSeq"
source_id: "gene-b1680"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1680"
  - "sufS"
---

# sufS

`gene.b1680`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1680`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sufS (gene.b1680) is a gene entity. It encodes sufS (protein.P77444). Encoded protein function: FUNCTION: Cysteine desulfurases mobilize the sulfur from L-cysteine to yield L-alanine, an essential step in sulfur metabolism for biosynthesis of a variety of sulfur-containing biomolecules. Component of the suf operon, which is activated and required under specific conditions such as oxidative stress and iron limitation. Acts as a potent selenocysteine lyase in vitro, that mobilizes selenium from L-selenocysteine. Selenocysteine lyase activity is however unsure in vivo. Can also desulfinate L-cysteine sulfinate (3-sulfino-L-alanine). {ECO:0000269|PubMed:10329673, ECO:0000269|PubMed:10829016, ECO:0000269|PubMed:11997471, ECO:0000269|PubMed:12089140, ECO:0000269|PubMed:12876288, ECO:0000269|PubMed:12941942}. EcoCyc product frame: G6906-MONOMER. EcoCyc synonyms: csdB, ynhB. Genomic coordinates: 1759303-1760523. EcoCyc protein note: SufS is one of three members of the NifS protein family in E. coli, the other two being CPLX0-7838 (G7454) and CPLX0-248 (G7325) . The protein was initially thought to function mainly as a pyridoxal 5'-phosphate (PLP)-dependent selenocysteine lyase with high specificity for L-selenocysteine...

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by rpoD (protein.P00579), oxyR (protein.P0ACQ4), iscR (protein.P0AGK8).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77444|protein.P77444]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sufS; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=sufS; function=+
- `activates` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `C` - regulator=IscR; target=sufS; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=sufS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005610,ECOCYC:G6906,GeneID:946185`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1759303-1760523:-; feature_type=gene
