---
entity_id: "gene.b3506"
entity_type: "gene"
name: "slp"
source_database: "NCBI RefSeq"
source_id: "gene-b3506"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3506"
  - "slp"
---

# slp

`gene.b3506`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3506`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

slp (gene.b3506) is a gene entity. It encodes slp (protein.P37194). Encoded protein function: FUNCTION: The induction of Slp may help to stabilize the outer membrane during carbon starvation and stationary phase. EcoCyc product frame: EG11890-MONOMER. Genomic coordinates: 3653961-3654527. EcoCyc protein note: Slp (starvation lipoprotein) is the product of the slp gene which forms an operon with the downstream gene dctR . Slp is believed to take part in acid resistance as expression increased when cells were grown at pH 5.5 and 4.5 under conditions known to induce glutamate-dependent acid resistance compared to pH 7.4 under the same conditions . During growth in acidic conditions, expression of Slp is negatively regulated by GadW, but positively regulated by GadXW, which are regulators of the two glutamate decarboxylase genes and the GABA APC transporter responsible for glutamate-dependent acid resistance . slp is highly induced by overexpression of EvgA , indirectly through its induction of YdeO expression , though slp was found to have a putative EvgA binding motif 542 base pairs upstream of its start codon . Under certain conditions, deletion of slp-dctR resulted in reduction of YdeO-induced acid resistance , though under conditions used to induce acid resistance naturally, slp-dctR was not necessary...

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579), gadX (protein.P37639), ydeO (protein.P76135), DNA-binding transcriptional dual regulator TorR-phosphorylated (protein.ecocyc.PHOSPHO-TORR).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37194|protein.P37194]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=slp; function=+
- `activates` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `C` - regulator=GadX; target=slp; function=+
- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=slp; function=+
- `activates` <-- [[protein.ecocyc.PHOSPHO-TORR|protein.ecocyc.PHOSPHO-TORR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=slp; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011451,ECOCYC:EG11890,GeneID:948022`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3653961-3654527:+; feature_type=gene
