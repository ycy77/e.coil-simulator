---
entity_id: "gene.b2369"
entity_type: "gene"
name: "evgA"
source_database: "NCBI RefSeq"
source_id: "gene-b2369"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2369"
  - "evgA"
---

# evgA

`gene.b2369`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2369`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

evgA (gene.b2369) is a gene entity. It encodes evgA (protein.P0ACZ4). Encoded protein function: FUNCTION: Member of the two-component regulatory system EvgS/EvgA (PubMed:10825546, PubMed:10923791, PubMed:9535079). The EvgS/EvgA system is involved in regulating the expression of glutamate-dependent acid resistance genes, acting in concert with transcription factors YdeO and GadE (PubMed:12694615, PubMed:15489450, PubMed:17998538). Regulates the expression of emrKY and safA-ydeO operons, gadE, yfdX and probably ydeP (PubMed:10923791, PubMed:11157960, PubMed:12694615, PubMed:15489450, PubMed:17998538). Binds directly to an 18 bp consensus sequence similar to 5'-AGCCTACACCTGTAAGAA-3' in the promoter region of safA/b1500 and other target genes, including its own operon, evgAS (PubMed:12694615, PubMed:15489450, PubMed:17998538). Also may control expression of multi-drug transporter mdtEF and other multi-drug efflux systems (PubMed:11157960, PubMed:11914367). Overexpression can confer resistance to antibiotics such as beta-lactams, probably as a result of up-regulation of multi-drug efflux systems (PubMed:12951338). {ECO:0000269|PubMed:10825546, ECO:0000269|PubMed:10923791, ECO:0000269|PubMed:11157960, ECO:0000269|PubMed:11914367, ECO:0000269|PubMed:12694615, ECO:0000269|PubMed:12951338, ECO:0000269|PubMed:15489450, ECO:0000269|PubMed:17998538, ECO:0000269|PubMed:9535079}...

## Biological Role

Repressed by carbon storage regulator CsrA (complex.ecocyc.CPLX0-7956), hns (protein.P0ACF8), csrA (protein.P69913), nac (protein.Q47005). Activated by rpoD (protein.P00579), evgA (protein.P0ACZ4), rpoS (protein.P13445).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACZ4|protein.P0ACZ4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=evgA; function=+
- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=evgA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=evgA; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7956|complex.ecocyc.CPLX0-7956]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=evgA; function=-
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `C` - regulator=carbon storage regulator CsrA; target=evgA; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=evgA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007817,ECOCYC:EG11609,GeneID:946841`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2483755-2484369:+; feature_type=gene
