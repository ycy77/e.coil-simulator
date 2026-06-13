---
entity_id: "gene.b3315"
entity_type: "gene"
name: "rplV"
source_database: "NCBI RefSeq"
source_id: "gene-b3315"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3315"
  - "rplV"
---

# rplV

`gene.b3315`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3315`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplV (gene.b3315) is a gene entity. It encodes rplV (protein.P61175). Encoded protein function: FUNCTION: This protein binds specifically to 23S rRNA; its binding is stimulated by other ribosomal proteins, e.g. uL4, bL17, and bL20. It is important during the early stages of 50S assembly. It makes multiple contacts with different domains of the 23S rRNA in the assembled 50S subunit and ribosome. {ECO:0000269|PubMed:13130133, ECO:0000269|PubMed:34504068, ECO:0000269|PubMed:7766155}.; FUNCTION: The globular domain of the protein is one of the proteins that surrounds the polypeptide exit tunnel on the outside of the subunit, while an extended beta-hairpin is found that penetrates into the center of the 70S ribosome where it lines the wall of the exit tunnel. Removal of most of this hairpin (residues 85-95) does not prevent its incorporation into 70S ribosomes (PubMed:13130133, PubMed:34504068). Two of the hairpin residues (Gly-91 and Ala-93) seem to be involved in translation elongation arrest of the SecM protein, as their replacement by larger amino acids alleviates the arrest (PubMed:11893334). In the TnaC-stalled ribosome makes a salt bridge to L-Trp (PubMed:34403461, PubMed:34504068). {ECO:0000269|PubMed:11893334, ECO:0000269|PubMed:13130133, ECO:0000269|PubMed:34403461, ECO:0000269|PubMed:34504068}. EcoCyc product frame: EG10882-MONOMER. EcoCyc synonyms: eryB...

## Biological Role

Repressed by fliX (gene.b4827). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P61175|protein.P61175]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rplV; function=+
- `represses` <-- [[gene.b4827|gene.b4827]] `RegulonDB` `S` - regulator=FliX; target=rplV; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010850,ECOCYC:EG10882,GeneID:947813`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3449901-3450233:-; feature_type=gene
