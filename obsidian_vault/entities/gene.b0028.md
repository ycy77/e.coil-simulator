---
entity_id: "gene.b0028"
entity_type: "gene"
name: "fkpB"
source_database: "NCBI RefSeq"
source_id: "gene-b0028"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0028"
  - "fkpB"
---

# fkpB

`gene.b0028`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0028`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fkpB (gene.b0028) is a gene entity. It encodes fkpB (protein.P0AEM0). Encoded protein function: FUNCTION: PPIases accelerate the folding of proteins (Probable). Substrate specificity investigated with 'Suc-Ala-Xaa-Pro-Phe-4-nitroanilide' where Xaa is the amino acid tested, was found to be Phe > Leu >> Ile > Lys = Ala > Trp > His >> Gln (PubMed:9188461). {ECO:0000269|PubMed:9188461, ECO:0000305}. EcoCyc product frame: EG11080-MONOMER. EcoCyc synonyms: slpA, yaaD. Genomic coordinates: 25826-26275. EcoCyc protein note: FkpB is a peptidyl-prolyl cis-trans isomerase (PPIase) of the FK506-binding protein type . FkpB also has chaperone activity; a number of ribosomal proteins appear to be natural substrates . Substrates were identified by pull-down assay and binding affinity measurements and include RpoE, RseA, RpsB and AphC . A crystal structure has been solved at 1.35 Å resolution. Serendipidously, the linker region of the purification tag of a different FkpB polypeptide is found in the chaperone binding groove of the insert-in-flap (IF) domain of FkpB, mimicing a chaperone substrate. A proline residue within the linker peptide appears to be specifically recognized and is important for binding . A solution structure of FkpB suggested that the orientation of the F37 residue is a reason for the moderate PPIase activity of FkpB; domain-swap experiments support this interpretation...

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEM0|protein.P0AEM0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fkpB; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=fkpB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000101,ECOCYC:EG11080,GeneID:944807`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:25826-26275:+; feature_type=gene
