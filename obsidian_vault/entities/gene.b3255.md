---
entity_id: "gene.b3255"
entity_type: "gene"
name: "accB"
source_database: "NCBI RefSeq"
source_id: "gene-b3255"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3255"
  - "accB"
---

# accB

`gene.b3255`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3255`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

accB (gene.b3255) is a gene entity. It encodes accB (protein.P0ABD8). Encoded protein function: FUNCTION: This protein is a component of the acetyl coenzyme A carboxylase complex; first, biotin carboxylase catalyzes the carboxylation of the carrier protein and then the transcarboxylase transfers the carboxyl group to form malonyl-CoA. {ECO:0000269|PubMed:4934522}. EcoCyc product frame: BCCP-MONOMER. EcoCyc synonyms: fabE. Genomic coordinates: 3405436-3405906. EcoCyc protein note: The accB gene encodes the biotin carboxyl carrier protein (BCCP), a component of acetyl CoA carboxylase . AccB is active as a dimer . The kinetics of the biotinylation reaction have been determined, and the N terminus does not appear to have any role in the modification . Biotinylation causes a large structural change in the C-terminal region of the protein . Biotinylation results in loss of conformational flexibility of the biotin interaction region ; a "thumb" domain comprising amino acids 94-101 fastens the biotin moiety to the surface of the protein and this interaction results in increased protein stability . This thumb domain is important for acetyl CoA carboxylase activity . Unbiotinylated AccB C-terminal domain dimerizes, and biotinylated AccB C-terminal domain is monomeric . AccB appears to interact with the C terminus of the BirA biotin ligase...

## Biological Role

Activated by rpoD (protein.P00579), fadR (protein.P0A8V6).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABD8|protein.P0ABD8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=accB; function=+
- `activates` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `S` - regulator=FadR; target=accB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010675,ECOCYC:EG10275,GeneID:947758`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3405436-3405906:+; feature_type=gene
