---
entity_id: "gene.b1160"
entity_type: "gene"
name: "iraM"
source_database: "NCBI RefSeq"
source_id: "gene-b1160"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1160"
  - "iraM"
---

# iraM

`gene.b1160`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1160`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

iraM (gene.b1160) is a gene entity. It encodes iraM (protein.P75987). Encoded protein function: FUNCTION: Inhibits RpoS proteolysis by regulating RssB activity, thereby increasing the stability of the sigma stress factor RpoS during magnesium starvation. May also be involved in the early steps of isoprenoid biosynthesis, possibly through its role as RssB regulator. {ECO:0000269|PubMed:18383615}. EcoCyc product frame: G6600-MONOMER. EcoCyc synonyms: elb1, ycgW, elbA. Genomic coordinates: 1211680-1212003. EcoCyc protein note: IraM is one of several small anti-adaptor proteins. In response to Mg2+ starvation, IraM inhibits proteolysis of the stationary phase sigma factor RPOS-MONOMER σS by interacting with EG12121-MONOMER RssB, which would normally target σS for degradation by the ClpXP protease . Each anti-adaptor protein interacts with RssB in a unique way . iraM expression is induced during Mg2+/Ca2+ starvation; regulation is dependent on PhoP . H-NS inhibits the expression of iraM . When placed on a multicopy plasmid, iraM creates a mutator phenotype . Expression of iraM is induced 40-fold upon exposure of cells to the biocide polyhexamehtylene biguanide (PHMB). Overexpression of iraM decreases the MIC of PHMB . IraM contributes to acid resistance via activation by the EvgSA two-component system and SafA...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75987|protein.P75987]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=iraM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003893,ECOCYC:G6600,GeneID:945729`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1211680-1212003:-; feature_type=gene
