---
entity_id: "protein.P77649"
entity_type: "protein"
name: "selO"
source_database: "UniProt"
source_id: "P77649"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "selO ydiU b1706 JW1696"
---

# selO

`protein.P77649`

## Static

- Type: `protein`
- Source: `UniProt:P77649`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Nucleotidyltransferase involved in the post-translational modification of proteins (PubMed:30270044, PubMed:32966796, PubMed:35532215, PubMed:35532216). It can catalyze the addition of adenosine monophosphate (AMP) or uridine monophosphate (UMP) to a protein, resulting in modifications known as AMPylation and UMPylation (PubMed:30270044, PubMed:32966796, PubMed:35532215, PubMed:35532216). It could be involved in stress resistance and play a crucial role in regulating essential bacterial processes, including flagella synthesis and iron uptake (PubMed:32966796, PubMed:35532215, PubMed:35532216). {ECO:0000269|PubMed:30270044, ECO:0000269|PubMed:32966796, ECO:0000269|PubMed:35532215, ECO:0000269|PubMed:35532216}.; FUNCTION: Can catalyze the transfer of adenosine 5'-monophosphate (AMP) to Ser, Thr and Tyr residues of target proteins (PubMed:30270044). In vitro, prefers ATP over other nucleotides as a cosubstrate (PubMed:30270044). Substrates include SelO itself, SucA, which is AMPylated on 'Thr-405', and GrxA, AMPylated on 'Tyr-13' (PubMed:30270044, PubMed:32966796). AMPylation of the grx family of enzymes may regulate protein S-glutathionylation levels in cells (PubMed:30270044). AMPylation is probably involved in redox homeostasis (PubMed:30270044). {ECO:0000269|PubMed:30270044, ECO:0000269|PubMed:32966796}...

## Biological Role

Catalyzes RXN0-7371 (reaction.ecocyc.RXN0-7371).

## Annotation

FUNCTION: Nucleotidyltransferase involved in the post-translational modification of proteins (PubMed:30270044, PubMed:32966796, PubMed:35532215, PubMed:35532216). It can catalyze the addition of adenosine monophosphate (AMP) or uridine monophosphate (UMP) to a protein, resulting in modifications known as AMPylation and UMPylation (PubMed:30270044, PubMed:32966796, PubMed:35532215, PubMed:35532216). It could be involved in stress resistance and play a crucial role in regulating essential bacterial processes, including flagella synthesis and iron uptake (PubMed:32966796, PubMed:35532215, PubMed:35532216). {ECO:0000269|PubMed:30270044, ECO:0000269|PubMed:32966796, ECO:0000269|PubMed:35532215, ECO:0000269|PubMed:35532216}.; FUNCTION: Can catalyze the transfer of adenosine 5'-monophosphate (AMP) to Ser, Thr and Tyr residues of target proteins (PubMed:30270044). In vitro, prefers ATP over other nucleotides as a cosubstrate (PubMed:30270044). Substrates include SelO itself, SucA, which is AMPylated on 'Thr-405', and GrxA, AMPylated on 'Tyr-13' (PubMed:30270044, PubMed:32966796). AMPylation of the grx family of enzymes may regulate protein S-glutathionylation levels in cells (PubMed:30270044). AMPylation is probably involved in redox homeostasis (PubMed:30270044). {ECO:0000269|PubMed:30270044, ECO:0000269|PubMed:32966796}.; FUNCTION: Under stress conditions, may act primarily as an uridylyltransferase that catalyzes the UMPylation of various proteins, including chaperones and transcription factors such as FlhDC and Fur (PubMed:32966796, PubMed:35532215, PubMed:35532216). Can also catalyze auto-UMPylation (PubMed:32966796). It can catalyze the Mn(2+)-dependent UMPylation on Tyr and His residues of chaperones such as GroEL, DnaK, HtpG and ClpB, leading to their inactivation (PubMed:32966796). Catalyzes the UMPylation on Ser-31 of the FlhC subunit of the major flagellar transcriptional regulator complex FlhDC (PubMed:35532215). UMPylated FlhDC complex completely loses its DNA binding activity, which inhibits the expression of secondary and tertiary flagellar genes, and interrupts flagellar synthesis (PubMed:35532215). Also catalyzes the UMPylation on His-118 residue of the major iron uptake regulator Fur, which destroys Fur dimers, (PubMed:35532216). Fur loses its DNA binding activity and therefore its repressor activity, which induces the expression of genes involved in iron uptake (PubMed:35532216). {ECO:0000269|PubMed:32966796, ECO:0000269|PubMed:35532215, ECO:0000269|PubMed:35532216}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7371|reaction.ecocyc.RXN0-7371]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1706|gene.b1706]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77649`
- `KEGG:ecj:JW1696;eco:b1706;ecoc:C3026_09770;`
- `GeneID:946219;`
- `GO:GO:0000287; GO:0005524; GO:0018117; GO:0030145; GO:0070733`
- `EC:2.7.7.-; 2.7.7.108`

## Notes

Protein nucleotidyltransferase SelO (EC 2.7.7.-) (Protein adenylyltransferase SelO) (EC 2.7.7.108) (Protein uridylyltransferase SelO) (EC 2.7.7.-) (Selenoprotein O homolog) (SelO)
