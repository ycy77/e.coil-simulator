---
entity_id: "protein.P0ACZ4"
entity_type: "protein"
name: "evgA"
source_database: "UniProt"
source_id: "P0ACZ4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "evgA b2369 JW2366"
---

# evgA

`protein.P0ACZ4`

## Static

- Type: `protein`
- Source: `UniProt:P0ACZ4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system EvgS/EvgA (PubMed:10825546, PubMed:10923791, PubMed:9535079). The EvgS/EvgA system is involved in regulating the expression of glutamate-dependent acid resistance genes, acting in concert with transcription factors YdeO and GadE (PubMed:12694615, PubMed:15489450, PubMed:17998538). Regulates the expression of emrKY and safA-ydeO operons, gadE, yfdX and probably ydeP (PubMed:10923791, PubMed:11157960, PubMed:12694615, PubMed:15489450, PubMed:17998538). Binds directly to an 18 bp consensus sequence similar to 5'-AGCCTACACCTGTAAGAA-3' in the promoter region of safA/b1500 and other target genes, including its own operon, evgAS (PubMed:12694615, PubMed:15489450, PubMed:17998538). Also may control expression of multi-drug transporter mdtEF and other multi-drug efflux systems (PubMed:11157960, PubMed:11914367). Overexpression can confer resistance to antibiotics such as beta-lactams, probably as a result of up-regulation of multi-drug efflux systems (PubMed:12951338). {ECO:0000269|PubMed:10825546, ECO:0000269|PubMed:10923791, ECO:0000269|PubMed:11157960, ECO:0000269|PubMed:11914367, ECO:0000269|PubMed:12694615, ECO:0000269|PubMed:12951338, ECO:0000269|PubMed:15489450, ECO:0000269|PubMed:17998538, ECO:0000269|PubMed:9535079}...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system EvgS/EvgA (PubMed:10825546, PubMed:10923791, PubMed:9535079). The EvgS/EvgA system is involved in regulating the expression of glutamate-dependent acid resistance genes, acting in concert with transcription factors YdeO and GadE (PubMed:12694615, PubMed:15489450, PubMed:17998538). Regulates the expression of emrKY and safA-ydeO operons, gadE, yfdX and probably ydeP (PubMed:10923791, PubMed:11157960, PubMed:12694615, PubMed:15489450, PubMed:17998538). Binds directly to an 18 bp consensus sequence similar to 5'-AGCCTACACCTGTAAGAA-3' in the promoter region of safA/b1500 and other target genes, including its own operon, evgAS (PubMed:12694615, PubMed:15489450, PubMed:17998538). Also may control expression of multi-drug transporter mdtEF and other multi-drug efflux systems (PubMed:11157960, PubMed:11914367). Overexpression can confer resistance to antibiotics such as beta-lactams, probably as a result of up-regulation of multi-drug efflux systems (PubMed:12951338). {ECO:0000269|PubMed:10825546, ECO:0000269|PubMed:10923791, ECO:0000269|PubMed:11157960, ECO:0000269|PubMed:11914367, ECO:0000269|PubMed:12694615, ECO:0000269|PubMed:12951338, ECO:0000269|PubMed:15489450, ECO:0000269|PubMed:17998538, ECO:0000269|PubMed:9535079}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (18)

- `activates` --> [[gene.b1499|gene.b1499]] `RegulonDB` `S` - regulator=EvgA; target=ydeO; function=+
- `activates` --> [[gene.b1500|gene.b1500]] `RegulonDB` `S` - regulator=EvgA; target=safA; function=+
- `activates` --> [[gene.b1501|gene.b1501]] `RegulonDB` `S` - regulator=EvgA; target=ydeP; function=+
- `activates` --> [[gene.b2085|gene.b2085]] `RegulonDB` `S` - regulator=EvgA; target=yegR; function=+
- `activates` --> [[gene.b2367|gene.b2367]] `RegulonDB` `S` - regulator=EvgA; target=emrY; function=+
- `activates` --> [[gene.b2368|gene.b2368]] `RegulonDB` `S` - regulator=EvgA; target=emrK; function=+
- `activates` --> [[gene.b2369|gene.b2369]] `RegulonDB` `S` - regulator=EvgA; target=evgA; function=+
- `activates` --> [[gene.b2370|gene.b2370]] `RegulonDB` `S` - regulator=EvgA; target=evgS; function=+
- `activates` --> [[gene.b2371|gene.b2371]] `RegulonDB` `S` - regulator=EvgA; target=yfdE; function=+
- `activates` --> [[gene.b2372|gene.b2372]] `RegulonDB` `S` - regulator=EvgA; target=yfdV; function=+
- `activates` --> [[gene.b2373|gene.b2373]] `RegulonDB` `S` - regulator=EvgA; target=oxc; function=+
- `activates` --> [[gene.b2374|gene.b2374]] `RegulonDB` `S` - regulator=EvgA; target=frc; function=+
- `activates` --> [[gene.b2375|gene.b2375]] `RegulonDB` `S` - regulator=EvgA; target=yfdX; function=+
- `activates` --> [[gene.b3512|gene.b3512]] `RegulonDB` `S` - regulator=EvgA; target=gadE; function=+
- `activates` --> [[gene.b3513|gene.b3513]] `RegulonDB` `S` - regulator=EvgA; target=mdtE; function=+
- `activates` --> [[gene.b3514|gene.b3514]] `RegulonDB` `S` - regulator=EvgA; target=mdtF; function=+
- `activates` --> [[gene.b4718|gene.b4718]] `RegulonDB` `S` - regulator=EvgA; target=gadF; function=+
- `activates` --> [[gene.b4781|gene.b4781]] `RegulonDB` `S` - regulator=EvgA; target=evgL; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b2369|gene.b2369]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACZ4`
- `KEGG:ecj:JW2366;eco:b2369;ecoc:C3026_13175;`
- `GeneID:75172487;75202562;946841;`
- `GO:GO:0000160; GO:0005829; GO:0006355; GO:0043565`

## Notes

DNA-binding transcriptional activator EvgA (Response regulator EvgA) (Transcriptional regulatory protein EvgA)
